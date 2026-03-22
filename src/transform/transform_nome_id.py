from src.extract.csv_deputados import csv_deputados
from src.transform.transform_valortotal_despesas import transform_valortotal_despesas
import polars as pl

def transform_nome_id() -> pl.DataFrame:
    """ Filtrou os dados dos deputados para obter somente o nome e o id dos 20 deputados que mais gastaram, utilizando como a base os dados das despesas já limpos.

    Returns:
        pl.DataFrame: Retorna um dataframe contendo os nomes e ids dos deputados.
    """
    df_deputados = csv_deputados()
    df_despesas = transform_valortotal_despesas()
    df_id_dep_despesas = df_despesas.select(['id']).to_series().to_list()
    
    deputados_filtrados = (
        df_deputados
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id', 'nomeCivil'])
    )
    return deputados_filtrados