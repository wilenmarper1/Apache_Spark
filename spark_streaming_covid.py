# spark_streaming_covid.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

spark = SparkSession.builder.appName("KafkaSparkStreamingCovid").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("country", StringType()),
    StructField("confirmed", IntegerType()),
    StructField("deaths", IntegerType()),
    StructField("recovered", IntegerType()),
    StructField("region", StringType()),
    StructField("timestamp", TimestampType())
])

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "covid_data") \
    .load()

parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Agrupar por región y ventana de tiempo (1 minuto)
windowed = parsed.groupBy(
    window(col("timestamp"), "1 minute"),
    col("region")
).sum("confirmed", "deaths", "recovered")

query = windowed.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()
