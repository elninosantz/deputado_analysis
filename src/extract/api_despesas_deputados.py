import requests

def fetch_despesas_deputados(id_deputados: int) -> list[dict]: 
    """ Consulta despesas de deputados da API, dos anos 2023 até 2026, através do ID.
    
    :return:
        list
    """
    response = requests.get(
    f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputados}/despesas?ano=2023,2024,2025,2026&ordem=ASC&ordenarPor=ano',
    )

    response.raise_for_status()
    despesas_raw = response.json()
    
    return despesas_raw['dados']
