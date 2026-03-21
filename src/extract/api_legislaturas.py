import requests


def fetch_legislatura() -> dict:
    """ Consulta dados de legislatura na API


    :return:
        dict
    """

    session = requests.Session()
    headers = {
        'accept': 'application/json',
    }

    response = session.get('https://dadosabertos.camara.leg.br/api/v2/legislaturas/57', headers=headers)
    response.raise_for_status()
    legislatura_raw = response.json()['dados']
    return legislatura_raw

