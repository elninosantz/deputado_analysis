import polars as pl

def extract_csv_despesas() -> pl.DataFrame:
    """Extracts deputy expenses data from the CSV file.

    Returns:
        pl.DataFrame: DataFrame containing the extracted deputy expenses data from the CSV file.
    """
    df = pl.read_csv('data/raw/despesas_deputados.csv')
    return df