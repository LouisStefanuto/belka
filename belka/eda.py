import polars as pl

# Define the path to your Parquet file
parquet_file = "data/test.parquet"

# Read Parquet file in chunks
df = pl.read_parquet(parquet_file)

print(df)
