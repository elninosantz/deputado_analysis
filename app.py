from src.load.save_csv_despesas import save_csv_despesas
from src.transform.cleaning_despesas import get_data_despesas
from src.transform.transform_valortotal_despesas import transform_valortotal_despesas
import polars as pl

if __name__ == "__main__":
    valor = transform_valortotal_despesas()
    
    print(valor)