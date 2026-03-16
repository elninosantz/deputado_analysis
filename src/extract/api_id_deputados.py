import requests


def fetch_deputados_raw() -> list[dict]:
    """ Consulta os dados dos deputados na API.

    :return:
        list: contendo os dados de deputados
    """

    session = requests.Session()
    params = {
        'idLegislatura': '57',
        'ordem': 'ASC',
        'ordenarPor': 'nome',
    }

    response = session.get('https://dadosabertos.camara.leg.br/api/v2/deputados', params=params)
    response.raise_for_status()
    return response.json()['dados']
