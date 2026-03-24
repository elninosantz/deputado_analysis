from src.extract.csv_despesas_deputados import extract_csv_despesas
import polars as pl

despesas_raw = extract_csv_despesas()

def transform_valortotal_despesas() -> pl.DataFrame:
    """Groups deputy data by ID and sums net expense values to get total spent per deputy.

    Returns:
        pl.DataFrame: DataFrame with deputy IDs and total amount spent by each deputy.
    """
    
    top20_mais_gastos = (
            despesas_raw
            .group_by('id')
            .agg(pl.col('valorLiquido').sum())
            .rename({'valorLiquido': 'valor_total'})
            .sort('valor_total', descending=True)
            .head(99)
    )
    return top20_mais_gastos

def transform_valortotal_despesas_ano() -> pl.DataFrame:
    """Groups deputy data by ID and year, summing net expense values per deputy per year.

    Returns:
        pl.DataFrame: DataFrame with deputy IDs, year, and total spent per deputy per year.
    """
    
    anos_mais_gastos = (
            despesas_raw
            .group_by(['id', 'ano'])
            .agg(pl.col('valorLiquido').sum())
            .rename({'valorLiquido': 'valor_total'})
            .sort('valor_total', descending=True)
    )
    return anos_mais_gastos