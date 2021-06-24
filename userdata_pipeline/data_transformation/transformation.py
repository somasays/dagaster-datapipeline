from pyspark.sql.session import SparkSession


class Transformer:
    """Data Transformer Python Class"""

    def __init__(self, spark: SparkSession, ingested_input_path: str, transformation_output_path: str):
        self.spark = spark
        self.ingested_input_path = ingested_input_path
        self.transformation_output_path = transformation_output_path

    def run(self):
        # Setup: read all input CSV
        schema = "firstname string, surname string"
        return (self.spark.read.format("csv")
                .schema(schema)
                .load(self.ingested_input_path)
                .drop('surname')
                .write.format("csv")
                .mode("overwrite")
                .save(self.transformation_output_path))
