from src.extract.api_despesas_deputados import fetch_despesas_deputados
import pandas as pd

def get_id_deputados():
    deputados = pd.read_csv('data/raw/deputados.csv')
    id_deputados = deputados['id'].to_list()
    
    return id_deputados
    


def get_data_despesas():
    id_deputados = get_id_deputados()
    for id_ in id_deputados:
        despesas_raw = fetch_despesas_deputados(id_)
        for despesas in despesas_raw:
            ano = despesas['ano']
            tipo_de_despesas = despesas['tipoDespesa']
            valor = despesas['valorLiquido']
            print(f'''
#################################################3
Ano da Despesa: {ano}
O que foi a despesa: {tipo_de_despesas}
Valor Liquido da Despesa: {valor}
                  ''')
            break
        

     