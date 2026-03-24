from src.extract.api_deputados import fetch_details_deputados

def get_data_deputados() -> dict[int, dict]:
    """Extracts detailed deputy data from raw API data.

    Processes the raw deputy data to include only active deputies with their
    civil name, state abbreviation, and party abbreviation.

    Returns:
        dict[int, dict]: A dictionary mapping deputy IDs to their processed data.
    """
    deputados_raw = fetch_details_deputados()
    processed_deputados = {}
    for id_, dados in deputados_raw.items():
        nome = dados['nomeCivil']
        ultimo_status = dados['ultimoStatus']
        situacao = ultimo_status['situacao']
        if situacao == "Exercício":
            processed_deputados[id_] = {
                'nomeCivil': nome,
                'siglaUF': ultimo_status['siglaUf'],
                'siglaPartido': ultimo_status['siglaPartido'],
            }

    return processed_deputados

