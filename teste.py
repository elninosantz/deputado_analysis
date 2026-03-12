import requests

def id_deputados() -> dict:
    """ Retorna o id de deputados

    Consulta dados de deputados, utilizando como parametro de consulta principal, estrutura temporal:
    dataInicio: inicio dos dados
    dataFim: fim dos dados

    Args:
        sem argumentos
    Returns:
        Dicionario contendo ID de deputados
    """
    ids_deputados = {}
    headers = {
        'accept': 'application/json',
    }

    params = {
        'dataInicio': '2022-01-01',
        'dataFim': '2026-03-20',
        'ordem': 'ASC',
        'ordenarPor': 'nome',
    }

    response = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados', params=params, headers=headers).json()
    dataframe =  response['dados']
    ids_deputados['ids_deputados'] = []
    for item in dataframe:
        ids_deputados['ids_deputados'].append(item['id'])
    return ids_deputados

idss_deputados = id_deputados()
print(idss_deputados)