from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from automationpbtnopythontrue00.config.ConfigStore import *
from automationpbtnopythontrue00.functions import *
from prophecy.utils import *
from automationpbtnopythontrue00.graph import *

def pipeline(spark: SparkSession) -> None:
    df_s3_source_dataset = s3_source_dataset(spark)
    create_lookup_table(spark, df_s3_source_dataset)
    df_select_from_temp_view = select_from_temp_view(spark, df_s3_source_dataset)
    df_reformatted_customer_data = reformatted_customer_data(spark, df_s3_source_dataset)
    df_print_execution_message = print_execution_message(spark, df_reformatted_customer_data)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("AutomationPBT-pythontrue00").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/AutomationPBTNo-pythontrue00")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/AutomationPBTNo-pythontrue00", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
