from src.transform.cleaning_deputados_id import get_id_deputados
import requests


def fetch_details_deputados() -> dict[int, dict]:
    """Consulta de dados detalhados dos deputados na API.

    :return:
        dict: dados dos deputados
    """

    ids_deputados = get_id_deputados()
    deputados_raw = {}
    session = requests.Session()

    for id_ in ids_deputados:
        response = session.get(f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_}')
        response.raise_for_status()
        deputados_raw[id_] = response.json()['dados']

    return deputados_raw

