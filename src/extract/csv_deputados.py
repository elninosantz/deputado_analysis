import polars as pl

def csv_deputados() -> pl.DataFrame:
    """ Função pra extrair os dados do arquivo CSV de deputados.

    Returns:
        pl.DataFrame: DataFrame contendo os dados extraídos do arquivo CSV de deputados.
    """
    df = pl.read_csv('data/raw/deputados.csv')
    return df