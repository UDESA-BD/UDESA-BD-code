from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local') \
    .appName('test') \
    .getOrCreate()

# Extraemos el esquema
esquema = spark.read.parquet("hdfs://namenode:8020/bicis/1/bicis0.parquet").schema

# Nos conectamos al dataset
df = spark.read.load("hdfs://namenode:8020/bicis/*", format='parquet', schema=esquema)

# Utilizamos Spark SQL, que nos brinda un DataFrame con numerosos métodos
# Documentación: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html
