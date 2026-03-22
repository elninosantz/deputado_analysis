from src.transform.transform_nome_id import transform_nome_id

import polars as pl

if __name__ == "__main__":
    df = transform_nome_id()
    print(df)