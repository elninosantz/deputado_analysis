from src.extract.api_despesas_deputados import fetch_despesas_deputados
import pandas as pd

def get_id_deputados() -> list[int]:
    """ Lê os dados csv e retorna como lista os id dos deputados

    :returns:
        list: ids dos deputados
    """
    deputados = pd.read_csv('data/raw/deputados.csv')
    id_deputados = deputados['id'].to_list()
    
    return id_deputados
    


def get_data_despesas() -> dict[int, dict]:
    """ Extrai os dados das despesas - valor das despesas, tipos de despesas, e ano das despesas
      dos deputados através do ID.
    
      :return:
        dict
    """ 
    despesas = {}
    id_deputados = get_id_deputados()
    for id_ in id_deputados:
        despesas_raw = fetch_despesas_deputados(id_)
        for despesas in despesas_raw:
            ano = despesas['ano']
            tipo_de_despesas = despesas['tipoDespesa']
            valor = despesas['valorLiquido']
            despesas[id_] = {
                'ano_despesa': ano,
                'tipo_de_despesa': tipo_de_despesas,
                'valor': valor
            }
    return despesas

     