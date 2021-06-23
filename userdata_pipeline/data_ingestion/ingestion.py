from pyspark.sql import DataFrame
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *

# ---------- Part II: Business Logic (for Part I, see data_ingestion/config.py) ---------- #


class Ingester:
    """Data Ingester Python Class"""

    def __init__(self, spark: SparkSession, parameters: "dict[str, str]"):
        self.spark = spark
        self.parameters = parameters
        return

    def run(self) -> None:
        kwargs = {"format": "csv", "sep": ",", "inferSchema": "true", "header": "true"}

        names_df = self.spark.read.load(self.parameters["names_input_path"], **kwargs)
        names_df.write.format("csv").mode("overwrite").save(self.parameters["names_output_path"])
        return
