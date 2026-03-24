import requests


def fetch_deputados_raw() -> list[dict]:
    """Fetches raw deputy data from the API.

    Returns:
        list[dict]: A list of dictionaries containing deputy data.
    """
    session = requests.Session()
    params = {
        'idLegislatura': '57',
        'ordem': 'ASC',
        'ordenarPor': 'nome',
    }

    response = session.get('https://dadosabertos.camara.leg.br/api/v2/deputados', params=params)
    response.raise_for_status()
    data = response.json()['dados']
    return data

