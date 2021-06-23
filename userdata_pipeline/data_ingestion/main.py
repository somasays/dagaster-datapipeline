import os

from pyspark.sql import SparkSession

from userdata_pipeline.data_ingestion import job_parameters
from data_ingestion.ingestion import Ingester

spark = SparkSession \
    .builder \
    .appName("Glue Data Ingestion") \
    .getOrCreate()

Ingester(spark, job_parameters).run()

print()
print("Spark Job Complete")
