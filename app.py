from src.load.save_csv_slicing import save_csv_nome_id, save_csv_id_uf, save_csv_id_partido
from src.load.save_csv_valor_total_despesa import save_csv_os_mais_gastos_filtrados

import polars as pl

if __name__ == "__main__":
    save_csv_os_mais_gastos_filtrados()