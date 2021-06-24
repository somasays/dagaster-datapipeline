# start-snippet
from dagster_aws.emr import emr_pyspark_step_launcher
from dagster_aws.s3 import s3_intermediate_storage, s3_resource
from dagster_pyspark import DataFrame as DagsterPySparkDataFrame
from dagster_pyspark import pyspark_resource
from pyspark.sql import DataFrame
from data_ingestion.ingestion import Ingester
from data_transformation.transformation import Transformer
import os
from datetime import datetime

from dagster import (
    ModeDefinition,
    make_python_type_usable_as_dagster_type,
    pipeline,
    repository,
    solid,
)

from dagster.core.definitions.no_step_launcher import no_step_launcher

# Make pyspark.sql.DataFrame map to dagster_pyspark.DataFrame
make_python_type_usable_as_dagster_type(python_type=DataFrame, dagster_type=DagsterPySparkDataFrame)


def get_partitioned_part(output_path):
    today = datetime.today()
    date = today.strftime('%Y-%m-%d')
    time = today.strftime('%H:%M:%S')
    return f"{output_path}/{date}/{time}"


@solid(
    required_resource_keys={"pyspark", "pyspark_step_launcher"},
    config_schema={"input_file_path": str, "output_file_path": str}
)
def ingest(context):
    input_path: str = context.solid_config["input_file_path"]
    output_path_timestamp: str = get_partitioned_part(context.solid_config["output_file_path"])
    spark = context.resources.pyspark.spark_session
    Ingester(spark=spark, input_path=input_path, output_path=output_path_timestamp).run()
    return output_path_timestamp


@solid(
    required_resource_keys={"pyspark", "pyspark_step_launcher"},
    config_schema={"transformation_output_path": str}
)
def transform(context, output_path_timestamp_from_ingestion):
    spark = context.resources.pyspark.spark_session
    Transformer(spark=spark, ingested_input_path=output_path_timestamp_from_ingestion,
                transformation_output_path=get_partitioned_part(
                    context.solid_config["transformation_output_path"])).run()


emr_mode = ModeDefinition(
    name="emr",
    resource_defs={
        "pyspark_step_launcher": emr_pyspark_step_launcher.configured(
            {
                "cluster_id": {"env": "EMR_CLUSTER_ID"},
                "local_pipeline_package_path": os.path.dirname(os.path.realpath(__file__)),
                "deploy_local_pipeline_package": True,
                "region_name": "eu-central-1",
                "staging_bucket": "dagster-scratch-80542c3",
            }
        ),
        "pyspark": pyspark_resource,
        "s3": s3_resource,
    },
    intermediate_storage_defs=[
        s3_intermediate_storage.configured(
            {"s3_bucket": "dagster-scratch-80542c3", "s3_prefix": "simple-pyspark"}
        )
    ],
)

local_mode = ModeDefinition(
    name="local",
    resource_defs={"pyspark_step_launcher": no_step_launcher, "pyspark": pyspark_resource},
)


@pipeline(mode_defs=[emr_mode, local_mode])
def my_pipeline():
    transform(ingest())


@repository
def emr_pyspark_example():
    return [my_pipeline]
