# Transform raw JSON using PySpark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('FlightsTransform').getOrCreate()
df = spark.read.json('raw_flights.json')
df.printSchema()
df.write.mode('overwrite').parquet('transformed_flights')
print('✅ Transformation complete')
