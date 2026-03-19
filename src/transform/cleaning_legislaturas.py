from src.extract.api_legislaturas import fetch_legislatura


def get_data_legislaturas() -> str:
    """Consulta a API e retorna a descrição textual da legislatura vigente.

    Returns:
        str: Frase com o número e o período da legislatura atual.
    """
    legislatura_raw: dict[str, str] = fetch_legislatura()

    id_legislatura: str = legislatura_raw['id']
    data_inicio: str = legislatura_raw['dataInicio']
    data_fim: str = legislatura_raw['dataFim']

    base_temporal_legislatura: str = (
        f'Os dados analisados referem-se aos deputados da {id_legislatura}ª Legislatura, '
        f'correspondente ao período de {data_inicio} a {data_fim}.'
    )

    return base_temporal_legislatura