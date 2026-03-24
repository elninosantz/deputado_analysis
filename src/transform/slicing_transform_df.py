from src.extract.csv_deputados import csv_deputados
from src.transform.transform_valortotal_despesas import transform_valortotal_despesas
import polars as pl

df_deputados = csv_deputados()
df_despesas = transform_valortotal_despesas()
df_id_dep_despesas = df_despesas.select(['id']).to_series().to_list()


def transform_maiores_gastos():
    maiores_gastos = pl.read_csv('data/raw/maiores_gastos.csv')
    maiores_gastos_filtrados = (
        maiores_gastos
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id','tipoDespesa','valorLiquido','ranking'])
    )
    return maiores_gastos_filtrados

def transform_nome_id() -> pl.DataFrame:
    """ Filtrou os dados dos deputados para obter somente o nome e o id dos 20 deputados que mais gastaram, utilizando como a base os dados das despesas já limpos.

    Returns:
        pl.DataFrame: Retorna um dataframe contendo os nomes e ids dos deputados.
    """

    deputados_filtrados_nome_id = (
        df_deputados
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id', 'nomeCivil'])
    )
    return deputados_filtrados_nome_id



def transform_id_uf() -> pl.DataFrame:
    """ Filtrou os dados dos deputados para obter somente o id e a uf dos 20 deputados que mais gastaram, utilizando como a base os dados das despesas já limpos.

    Returns:
        pl.DataFrame: Retorna um dataframe contendo os ids e ufs dos deputados.
    """

    deputados_filtrados_id_uf = (
        df_deputados
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id', 'siglaUF'])
    )
    return deputados_filtrados_id_uf



def transform_id_partido() -> pl.DataFrame:
    """ Filtrou os dados dos deputados para obter somente o id e o partido dos 20 deputados que mais gastaram, utilizando como a base os dados das despesas já limpos.

    Returns:
        pl.DataFrame: Retorna um dataframe contendo os ids e partidos dos deputados.
    """

    deputados_filtrados_id_partido = (
        df_deputados
        .filter(pl.col('id').is_in(df_id_dep_despesas))
        .select(['id', 'siglaPartido'])
    )
    return deputados_filtrados_id_partido