import requests

def id_deputados() -> dict[str, str]:
    """ Retorna o id de deputados

    Consulta dados de deputados, utilizando como parametro de consulta principal, estrutura temporal:
    dataInicio: inicio dos dados
    dataFim: fim dos dados

    :return:
        dict: contendo ID de deputados
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


def df_deputados() -> dict[str, str]:
    """Coleta de dados dos deputados

    Consulta de dados na api, passando os parametros de id de cada deputado e extraindo os dados
    dos deputados.

    :return:
        dict: dados dos deputados
    """

    ids_deputados = id_deputados()
    deputados_raw = {}
    for ids in ids_deputados['ids_deputados']:
        headers = {
            'accept': 'application/json',
        }

        response = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ids}',headers=headers).json()
        deputados_raw[ids] = response['dados']
    return deputados_raw
