import pandas as pd
from src.transform.cleaning_despesas import get_data_despesas

def save_csv_despesas() -> None:
    """ Salva os dados de despesas dos deputados, orientados a index em csv
    
    :return:
        None
    """ 
    despesas_raw = get_data_despesas()
    df = pd.DataFrame.from_dict(despesas_raw, orient='index')
    df.index.name = 'id'
    df.to_csv('data/raw/despesas_deputados.csv')



