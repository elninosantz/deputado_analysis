from src.extract.csv_despesas_deputados import extract_csv_despesas
import polars as pl

despesas_raw = extract_csv_despesas()

def transform_valortotal_despesas() -> pl.DataFrame:
    """ Função agrupa os dados de id dos deputados, e soma os valores de despesas liquidos para obter o valor total gasto pelo deputado, na sua legislatura.

    Returns:
        pl.DataFrame: Retorna um Dataframe contendo colunas de id dos deputados e valor total gasto por cada deputado.
    """
    
    top20_mais_gastos = (
            despesas_raw
            .group_by('id')
            .agg(pl.col('valorLiquido').sum())
            .rename({'valorLiquido': 'valor_total'})
            .sort('valor_total', descending=True)
            .head(20)
    )
    return top20_mais_gastos

def transform_valortotal_despesas_ano() -> pl.DataFrame:
    """ Função agrupa os dados de id dos deputados, ano e soma os valores de despesas liquidos para obter o valor total gasto por cada deputado em cada ano da sua legislatura.

    Returns:
        pl.DataFrame: Retorna um Dataframe contendo colunas de id dos deputados, ano e valor total gasto por cada deputado em cada ano.
    """
    
    anos_mais_gastos = (
            despesas_raw
            .group_by(['id', 'ano'])
            .agg(pl.col('valorLiquido').sum())
            .rename({'valorLiquido': 'valor_total'})
            .sort('valor_total', descending=True)
    )
    return anos_mais_gastos