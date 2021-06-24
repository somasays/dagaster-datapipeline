from pyspark.sql.session import SparkSession

# ---------- Part II: Business Logic (for Part I, see data_ingestion/config.py) ---------- #


class Ingester:
    """Data Ingester Python Class"""

    def __init__(self, spark: SparkSession, input_path: str, output_path: str):
        self.spark = spark
        self.input_path = input_path
        self.output_path = output_path
        return

    def run(self) -> None:
        kwargs = {"format": "csv", "sep": ",", "inferSchema": "true", "header": "true"}

        names_df = self.spark.read.load(self.input_path, **kwargs)
        names_df.write.format("csv").mode("overwrite").save(self.output_path)
        return
