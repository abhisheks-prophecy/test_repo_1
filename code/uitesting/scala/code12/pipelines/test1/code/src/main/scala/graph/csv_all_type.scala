package graph

import io.prophecy.libs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import config.ConfigStore._

object csv_all_type {

  def apply(spark: SparkSession): DataFrame =
    spark.read
      .format("csv")
      .option("header", false)
      .option("sep",    ",")
      .schema(
        StructType(
          Array(
            StructField("_c0", StringType, true),
            StructField("_c1", StringType, true),
            StructField("_c2", StringType, true),
            StructField("_c3", StringType, true),
            StructField("_c4", StringType, true),
            StructField("_c5", StringType, true),
            StructField("_c6", StringType, true),
            StructField("_c7", StringType, true),
            StructField("_c8", StringType, true),
            StructField("_c9", StringType, true)
          )
        )
      )
      .load("dbfs:/Prophecy/qa_data/csv/all_type_no_partition")

}
