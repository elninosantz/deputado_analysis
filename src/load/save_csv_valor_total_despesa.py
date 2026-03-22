from src.transform.transform_valortotal_despesas import transform_valortotal_despesas
import polars as pl

def save_csv_valor_total_despesa():
    df_despesas_total = transform_valortotal_despesas()
    df_despesas_total.write_csv('data/processed/valor_total_despesa.csv')
