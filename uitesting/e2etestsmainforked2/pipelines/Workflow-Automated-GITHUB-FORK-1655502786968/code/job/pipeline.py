from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Script_1 = Script_1(spark)
    df_Source_0 = Source_0(spark)
    df_Source_1 = Source_1(spark)
    df_Limit_1 = Limit_1(spark, df_Source_0)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    pipeline(spark)

if __name__ == "__main__":
    main()
