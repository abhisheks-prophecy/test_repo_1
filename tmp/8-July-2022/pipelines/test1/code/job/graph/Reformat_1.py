from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("account_flags"), 
        col("account_open_date"), 
        col("country_code"), 
        col("customer_id"), 
        col("email"), 
        col("first_name"), 
        col("last_name"), 
        col("phone")
    )
