import polars as pl

def extract_csv_despesas() -> pl.DataFrame:
    """ Função para extrair os dados do arquivo CSV de despesas dos deputados.

    Returns:
        pl.DataFrame: DataFrame contendo os dados extraídos do arquivo CSV de despesas dos deputados.
    """
    df = pl.read_csv('data/raw/despesas_deputados.csv')
    return df