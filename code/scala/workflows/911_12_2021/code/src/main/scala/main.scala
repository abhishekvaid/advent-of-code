import io.prophecy.libs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import config.ConfigStore._
import udfs.UDFs._
import udfs._
import graph._

object Main {

  def apply(spark: SparkSession): Unit = {
    val df_Reformat_0 = Reformat_0(spark)
    val df_Filter_0   = Filter_0(spark,   df_Reformat_0)
    val df_Filter_0_1 = Filter_0_1(spark, df_Filter_0)
  }

  def main(args: Array[String]): Unit = {
    import config._
    ConfigStore.Config = ConfigurationFactoryImpl.fromCLI(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Prophecy Workflow")
      .config("spark.default.parallelism", "4")
      .enableHiveSupport()
      .getOrCreate()
    apply(spark)
  }

}
