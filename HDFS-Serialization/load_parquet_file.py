import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.read_csv('archivos/trips_2024.csv', names=['id_recorrido', 'duracion_recorrido', 'fecha_origen_recorrido',
'id_estacion_origen', 'nombre_estacion_origen', 'direccion_estacion_origen', 
'long_estacion_origen', 'lat_estacion_origen', 'fecha_destino_recorrido', 'id_estacion_destino', 'nombre_estacion_destino', 'direccion_estacion_destino', 'long_estacion_destino', 'lat_estacion_destino', 'id_usuario', 'modelo_bicicleta', 'genero'])

parquet_table = pa.Table.from_pandas(df)

pq.write_to_dataset(
    parquet_table,
    root_path=f"hdfs://localhost/",
    basename_template="{i}.parquet",
    #partition_cols=["month", "day"]
)