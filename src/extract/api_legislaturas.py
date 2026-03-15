import requests

def legislatura() -> dict:
    headers = {
        'accept': 'application/json',
    }

    response = requests.get('https://dadosabertos.camara.leg.br/api/v2/legislaturas/57', headers=headers).json()
    dataframe = response['dados']
    return dataframe
