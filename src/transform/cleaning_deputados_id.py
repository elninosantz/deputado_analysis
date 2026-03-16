from src.extract.api_id_deputados import fetch_deputados_raw

def get_id_deputados() -> list[int]:
    """ Extrai os IDs dos deputados a partir dos dados brutos da API

    :return:
        List: contendo os ids dos deputados
    """
    ids_deputados = []
    deputados_raw = fetch_deputados_raw()
    for deputado in deputados_raw:
        ids_deputados.append(deputado['id'])

    return ids_deputados

