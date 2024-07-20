from pyspark import SparkContext, SparkConf

#################################################33
# Modo 1
# Creamos un contexto de Spark
# sc = SparkContext('local', 'test')
#
# Nos conectamos al cluster HDFS
# archivo = sc.textFile("hdfs://namenode:8020/trips_2024.csv")
#################################################33

#################################################33
# Modo 2
sc = SparkContext(master='yarn')
archivo = sc.textFile("/trips_2024.csv")
#################################################33

# Ejecutamos la tarea, en este caso contar la cantidad de líneas del archivo
archivo.count()

