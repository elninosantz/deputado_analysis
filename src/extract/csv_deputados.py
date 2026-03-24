import polars as pl

def csv_deputados() -> pl.DataFrame:
    """Extracts deputy data from the CSV file.

    Returns:
        pl.DataFrame: DataFrame containing the extracted deputy data from the CSV file.
    """
    df = pl.read_csv('data/raw/deputados.csv')
    return df