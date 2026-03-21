from src.extract.api_deputados import fetch_details_deputados

def get_data_deputados() -> dict[int, dict]:
    """ Extrai os dados detalhados dos deputados a partir dos dados brutos da API

    :return:
        dict
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

