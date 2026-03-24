import polars as pl

def maiores_gastos():
    df = pl.read_csv("data/raw/despesas_deputados.csv")
    valor_total = df.group_by("id").agg(pl.col("valorLiquido").sum())
    maisaparece = df.group_by('id', 'tipoDespesa').agg(pl.col('valorLiquido').sum())
    maisaparece = maisaparece.with_columns(
        pl.col("valorLiquido").rank(descending=True).over("id").alias("ranking")
    )
    top5 = maisaparece.filter(pl.col("ranking") <= 5)
    return top5