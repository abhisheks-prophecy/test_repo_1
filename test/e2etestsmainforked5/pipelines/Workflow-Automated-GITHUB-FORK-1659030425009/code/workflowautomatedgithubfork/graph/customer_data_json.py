from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from workflowautomatedgithubfork.config.ConfigStore import *
from workflowautomatedgithubfork.udfs.UDFs import *

def customer_data_json(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .schema(
          StructType([
            StructField("account_flags", StringType(), True), StructField("account_open_date", StringType(), True), StructField("country_code", StringType(), True), StructField("customer_id", StringType(), True), StructField("email", StringType(), True), StructField("first_name", StringType(), True), StructField("last_name", StringType(), True), StructField("phone", StringType(), True)
        ])
        )\
        .load("dbfs:/Prophecy/qa_data/json/CustomersDatasetInput.json")
