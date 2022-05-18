from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Source_0(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "dev":
        return spark.read\
            .schema(
              StructType([
                StructField("customer_id", StringType(), True), StructField("first_name", StringType(), True), StructField("last_name", StringType(), True), StructField("phone", StringType(), True), StructField("email", StringType(), True), StructField("country_code", StringType(), True), StructField("account_open_date", StringType(), True), StructField("account_flags", StringType(), True)
            ])
            )\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/Prophecy/qa_data/csv/CustomersDatasetInputWithHeader.csv")
    elif Config.fabricName == "dev_Second_fabric":
        return spark.read\
            .schema(StructType([StructField("a", BinaryType(), True)]))\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/Prophecy/qa_data/csv/CustomersDatasetInputWithHeader.csv")
    else:
        raise Exception("No valid dataset present to read fabric")
