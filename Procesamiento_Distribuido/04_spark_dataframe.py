from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, functions
from pyspark.sql import functions

spark = SparkSession.builder.master('local') \
    .appName('test') \
    .getOrCreate()

# Extraemos el esquema
esquema = spark.read.parquet("hdfs://namenode:8020/bicis/1/bicis0.parquet").schema

# Nos conectamos al dataset
df = spark.read.load("hdfs://namenode:8020/bicis/*", format='parquet', schema=esquema)

# Utilizamos Spark SQL, que nos brinda un DataFrame con dos formas de realizar consultas:
# - Utilizando SQL: https://spark.apache.org/docs/3.5.2/sql-getting-started.html#running-sql-queries-programmatically
# - Utilizando métodos propios de DataFrames: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html
