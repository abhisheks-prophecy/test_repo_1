from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customer_data_json = customer_data_json(spark)
    df_Limit_1 = Limit_1(spark, df_customer_data_json)
    df_customer_data_json_1 = customer_data_json_1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "9574/pipelines/Workflow-Automated-GITHUB-FORK-1657993057267")
    MetricsCollector.start(spark)
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
