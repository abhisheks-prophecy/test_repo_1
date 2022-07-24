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
    df_Script_1 = Script_1(spark)
    df_customer_data_parquet = customer_data_parquet(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "9728/pipelines/Workflow-Automated-GITHUB-FORK-1658128455966")
    
    MetricsCollector.start(spark = spark, pipelineId = "9728/pipelines/Workflow-Automated-GITHUB-FORK-1658128455966")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
