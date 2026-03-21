import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"
ANOS = "2023,2024,2025,2026"
HEADERS = {"accept": "application/json"}
TIMEOUT = 220


def create_session() -> requests.Session:
    """cria uma session configurada pra tentar de novo automaticamente quando a API falhar, esperando cada vez mais tempo entre as tentativas.

    Returns:
        requests.Session: Retorna uma session configurada para lidar continuamente com falhas temporárias da API.
    """
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def fetch_despesas_deputados(id_deputado: int, session: requests.Session | None = None) -> list:
    """Consulta despesas de um deputado da API da Câmara dos Deputados,
    dos anos 2023 até 2026, paginando automaticamente.

    :param id_deputado: ID do deputado na API.
    :param session: Session configurada para lidar com falhas temporárias.

    :return: Lista com todos os registros de despesas.
    """

    if session is None:
        session = create_session()

    despesas = []
    pagina = 1

    while True:
        response = requests.get(
            f"{BASE_URL}/deputados/{id_deputado}/despesas",
            headers=HEADERS,
            timeout=TIMEOUT,
            params={
                "ano": ANOS,
                "ordem": "ASC",
                "ordenarPor": "ano",
                "pagina": pagina,
                "itens": 100,
            },
        )
        response.raise_for_status()
        payload = response.json()

        despesas.extend(payload["dados"])

        links = {link["rel"]: link["href"] for link in payload["links"]}
        pagina += 1

        if links.get("self") == links.get("last"):
            break

    return despesas