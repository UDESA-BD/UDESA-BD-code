import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import fs

df = pd.read_csv('/tmp/trips_2024.csv', names=['id_recorrido', 'duracion_recorrido', 'fecha_origen_recorrido',
'id_estacion_origen', 'nombre_estacion_origen', 'direccion_estacion_origen', 
'long_estacion_origen', 'lat_estacion_origen', 'fecha_destino_recorrido', 'id_estacion_destino', 'nombre_estacion_destino', 'direccion_estacion_destino', 'long_estacion_destino', 'lat_estacion_destino', 'id_usuario', 'modelo_bicicleta', 'genero'])

tabla_pyarrow = pa.Table.from_pandas(df)

mi_hdfs = fs.HadoopFileSystem('namenode', port=8020, user='hadoop', replication=2)

pq.write_to_dataset(
    tabla_pyarrow,
    filesystem=mi_hdfs,
    root_path='/',
    basename_template="bicis{i}.parquet",
    partitioning=["genero"]
)
