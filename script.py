from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as t

def main():
    spark = SparkSession.builder.getOrCreate()

    df = spark.read.format("csv").option("header", "true").load("data/cars.csv")

    output = (
        df
        .groupBy("manufacturer_name")
        .agg(
            F.count("manufacturer_name").alias("count"),
            F.round(F.avg("year_produced")).cast(t.IntegerType()).alias("avg_year"),
            F.min(F.col("price_usd").cast(t.FloatType())).alias("min_price"),
            F.max("price_usd").cast(t.FloatType()).alias("max_price")
        )
    )

    output.coalesce(4).write.mode("overwrite").format("json").save("result.json")

main()