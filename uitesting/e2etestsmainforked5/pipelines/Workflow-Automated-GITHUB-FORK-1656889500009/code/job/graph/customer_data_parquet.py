from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def customer_data_parquet(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/Prophecy/qa_data/parquet/CustomersDatasetInput.parquet")
