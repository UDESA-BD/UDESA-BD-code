import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import fs

df = pd.read_csv('archivos/trips_2024.csv', names=['id_recorrido', 'duracion_recorrido', 'fecha_origen_recorrido',
'id_estacion_origen', 'nombre_estacion_origen', 'direccion_estacion_origen', 
'long_estacion_origen', 'lat_estacion_origen', 'fecha_destino_recorrido', 'id_estacion_destino', 'nombre_estacion_destino', 'direccion_estacion_destino', 'long_estacion_destino', 'lat_estacion_destino', 'id_usuario', 'modelo_bicicleta', 'genero'])

tabla_pyarrow = pa.Table.from_pandas(df)

pq.write_to_dataset(
    tabla_pyarrow,
    root_path=f"hdfs://localhost:8020",
    basename_template="/{i}.parquet",
    partition_cols=["genero"]
)

sist_arch = fs.HadoopFileSystem.from_uri('hdfs://localhost')


import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import fs
from hdfs import InsecureClient

hdfs_config = {
     "host" : "0.0.0.0",
     "port" : 8020,
     "user" : "hadoop"
}

HDFS_HOSTNAME = 'namenode'
HDFSCLI_PORT = 9870
HDFSCLI_CONNECTION_STRING = f'http://{HDFS_HOSTNAME}:{HDFSCLI_PORT}'
hdfs_client = InsecureClient(HDFSCLI_CONNECTION_STRING)

with hdfs_client.read('/hola') as reader:
    df = pd.read_csv(reader,sep=';')

df = pd.DataFrame([2,3,1], columns=["asqw"])
tabla_pyarrow = pa.Table.from_pandas(df)

sist_arch = fs.HadoopFileSystem.from_uri('hdfs://namenode:8020/?user=hadoop&replication=2')