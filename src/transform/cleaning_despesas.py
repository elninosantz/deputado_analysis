from src.extract.api_despesas_deputados import fetch_despesas_deputados
import polars as pl


def get_id_deputados() -> list[int]:
    """ Lê os dados csv e retorna como lista os id dos deputados

    :returns:
        list: ids dos deputados
    """
    deputados = pl.read_csv('data/raw/deputados.csv')
    id_deputados = deputados['id'].to_list()
    
    return id_deputados


def get_data_despesas() -> dict[int, list[dict]]:
    """ Extrai os dados das despesas dos deputados através do ID.
    
      :return: Dicionario contendo, valor das despesas, tipos de despesas e o ano das despesas
    """ 
    despesas_dos_deputados = {}
    id_deputados = get_id_deputados()
    for id_ in id_deputados:
        despesas_raw = fetch_despesas_deputados(id_)
        despesas_dos_deputados[id_] = [            
            {
                'tipoDespesa': despesa['tipoDespesa'],
                'valorLiquido': despesa['valorLiquido'],
                'ano': despesa['ano']
            }
            for despesa in despesas_raw
            ]
        
    return despesas_dos_deputados
