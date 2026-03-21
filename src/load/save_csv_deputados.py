from src.transform.cleaning_deputados import get_data_deputados
import polars as pl

def save_csv_deputados()-> None:
    """ Salva os dados dos deputados, orientados a index em csv
    
    :return:
        None
    """ 
    deputados_raw = get_data_deputados()
    registros = [{'id': id_, **dados} for id_, dados in deputados_raw.items()]
    df = pl.DataFrame(registros)
    df.write_csv('data/raw/deputados.csv')
