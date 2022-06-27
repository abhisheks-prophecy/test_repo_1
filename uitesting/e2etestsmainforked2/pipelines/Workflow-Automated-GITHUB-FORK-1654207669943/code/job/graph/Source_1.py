from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Source_1(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "dev":
        return spark.read.format("parquet").load("dbfs:/Prophecy/qa_data/parquet/CustomersDatasetInput.parquet")
    else:
        raise Exception("No valid dataset present to read fabric")
