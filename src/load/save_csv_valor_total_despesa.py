from src.transform.transform_valortotal_despesas import transform_valortotal_despesas, transform_valortotal_despesas_ano
from src.transform.slicing_transform_df import transform_maiores_gastos

import polars as pl

def save_csv_valor_total_despesa():
    """Saves the total expense values per deputy to CSV.

    Returns:
        None: Saves the file without returning a value.
    """
    df_despesas_total = transform_valortotal_despesas()
    df_despesas_total.write_csv('data/processed/valor_total_despesa.csv')

def save_csv_valor_total_anos():
    """Saves the total expense values per deputy per year to CSV.

    Returns:
        None: Saves the file without returning a value.
    """
    df_ano = transform_valortotal_despesas_ano()
    df_ano.write_csv('data/processed/valor_total_por_ano.csv')

def save_csv_os_mais_gastos_filtrados():
    """Saves the filtered top expenses data to CSV.

    Returns:
        None: Saves the file without returning a value.
    """
    df_gastos_mariores = transform_maiores_gastos()
    df_gastos_mariores.write_csv('data/processed/maiores_gastos_filtrados.csv')