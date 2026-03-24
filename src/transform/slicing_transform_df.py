from src.extract.csv_deputados import csv_deputados
from src.transform.transform_valortotal_despesas import transform_valortotal_despesas
import polars as pl

df_deputados = csv_deputados()
df_despesas = transform_valortotal_despesas()
df_id_dep_despesas = df_despesas.select(['id']).to_series().to_list()


def transform_maiores_gastos():
    """Filters the top expenses data to include only deputies with expense records.

    Returns:
        pl.DataFrame: Filtered DataFrame with ID, expense type, net value, and ranking.
    """
    maiores_gastos = pl.read_csv('data/raw/maiores_gastos.csv')
    maiores_gastos_filtrados = (
        maiores_gastos
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id','tipoDespesa','valorLiquido','ranking'])
    )
    return maiores_gastos_filtrados

def transform_nome_id() -> pl.DataFrame:
    """Filters deputy data to get names and IDs of the top spending deputies.

    Uses cleaned expense data as the base to filter deputies.

    Returns:
        pl.DataFrame: DataFrame containing deputy names and IDs.
    """
    deputados_filtrados_nome_id = (
        df_deputados
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id', 'nomeCivil'])
    )
    return deputados_filtrados_nome_id



def transform_id_uf() -> pl.DataFrame:
    """Filters deputy data to get IDs and states of the top spending deputies.

    Uses cleaned expense data as the base to filter deputies.

    Returns:
        pl.DataFrame: DataFrame containing deputy IDs and state abbreviations.
    """
    deputados_filtrados_id_uf = (
        df_deputados
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id', 'siglaUF'])
    )
    return deputados_filtrados_id_uf



def transform_id_partido() -> pl.DataFrame:
    """Filters deputy data to get IDs and parties of the top spending deputies.

    Uses cleaned expense data as the base to filter deputies.

    Returns:
        pl.DataFrame: DataFrame containing deputy IDs and party abbreviations.
    """
    deputados_filtrados_id_partido = (
        df_deputados
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id', 'siglaPartido'])
    )
    return deputados_filtrados_id_partido