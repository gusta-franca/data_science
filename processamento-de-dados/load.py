import pandas as pd
import duckdb

arquivo = "yellow_tripdata_2026-01. parquet"
df = pd.read_parquet(arquivo)
con = duckdb.connect()
con.execute(f"""
    CREATE TABLE corridas AS
    SELECT * FROM read_parquet(’{arquivo}’)
""")