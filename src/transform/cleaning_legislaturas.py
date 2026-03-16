from src.extract.api_legislaturas import fetch_legislatura

def get_data_legislaturas() -> str:
    """ Criando o embasamento para certificar a veracidade dos dados temporalmente

    :return:
        str: informação sobre legislatura
    """

    legislatura_raw = fetch_legislatura()
    id_legislatura = legislatura_raw['id']
    data_inicio = legislatura_raw['dataInicio']
    data_fim = legislatura_raw['dataFim']
    base_temporal_legislatura = f'Os dados analisados referem-se aos deputados da {id_legislatura}ª Legislatura, correspondente ao período de {data_inicio} a {data_fim}.'

    return base_temporal_legislatura



