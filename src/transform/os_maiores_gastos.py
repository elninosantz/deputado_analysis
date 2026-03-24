import polars as pl

def maiores_gastos():
    """Calculates the top 5 expense types per deputy based on total value.

    Reads deputy expenses data, groups by deputy ID and expense type,
    ranks the expense types by total value, and returns the top 5 for each deputy.

    Returns:
        pl.DataFrame: DataFrame with deputy ID, expense type, total value, and ranking.
    """
    df = pl.read_csv("data/raw/despesas_deputados.csv")
    valor_total = df.group_by("id").agg(pl.col("valorLiquido").sum())
    maisaparece = df.group_by('id', 'tipoDespesa').agg(pl.col('valorLiquido').sum())
    maisaparece = maisaparece.with_columns(
        pl.col("valorLiquido").rank(descending=True).over("id").alias("ranking")
    )
    top5 = maisaparece.filter(pl.col("ranking") <= 5)
    return top5