from src.transform.cleaning_deputados import get_data_deputados
import pandas as pd

def save_csv_deputados()-> None:
    """ Salva os dados dos deputados, orientados a index em csv
    
    :return:
        None
    """ 
    deputados_raw = get_data_deputados()
    df = pd.DataFrame.from_dict(deputados_raw, orient='index')
    df.index.name = 'id'
    df.to_csv('data/raw/deputados.csv')

