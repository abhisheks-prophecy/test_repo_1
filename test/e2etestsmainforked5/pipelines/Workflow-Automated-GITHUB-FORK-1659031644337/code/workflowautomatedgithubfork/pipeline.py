from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from workflowautomatedgithubfork.config.ConfigStore import *
from workflowautomatedgithubfork.udfs.UDFs import *
from prophecy.utils import *
from workflowautomatedgithubfork.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customer_data_json = customer_data_json(spark)
    df_Limit_1 = Limit_1(spark, df_customer_data_json)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "10926/pipelines/Workflow-Automated-GITHUB-FORK-1659031644337")
    MetricsCollector.start(spark = spark, pipelineId = "10926/pipelines/Workflow-Automated-GITHUB-FORK-1659031644337")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
