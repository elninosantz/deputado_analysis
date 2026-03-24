from src.extract.api_id_deputados import fetch_deputados_raw

def get_id_deputados() -> list[int]:
    """Extracts deputy IDs from raw API data.

    Returns:
        list[int]: A list of deputy IDs.
    """
    ids_deputados = []
    deputados_raw = fetch_deputados_raw()
    for deputado in deputados_raw:
        ids_deputados.append(deputado['id'])

    return ids_deputados
