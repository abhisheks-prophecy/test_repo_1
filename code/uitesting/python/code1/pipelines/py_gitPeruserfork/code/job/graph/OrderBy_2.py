from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def OrderBy_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(
        col("order_id").asc(), 
        col("customer_id").asc(), 
        col("order_status").asc(), 
        col("order_category").asc(), 
        col("order_date").asc(), 
        col("amount").asc()
    )
