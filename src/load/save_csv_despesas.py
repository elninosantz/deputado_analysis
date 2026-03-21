import polars as pl
from src.transform.cleaning_despesas import get_data_despesas

def save_csv_despesas() -> None:
    """ Salva os dados de despesas dos deputados, orientados a index em csv
    
    :return:
        None
    """ 
    linhas = []
    despesas_raw = get_data_despesas()
    for id_, despesas in despesas_raw.items():
        for despesa in despesas:
            linhas.append({'id': id_, **despesa})

    
    df = pl.DataFrame(linhas)
    df.write_csv('data/raw/despesas_deputados.csv')


