import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"
ANOS = "2023,2024,2025,2026"
HEADERS = {"accept": "application/json"}
TIMEOUT = 220


def create_session() -> requests.Session:
    """Creates a session configured to retry automatically on API failures, with increasing wait times.

    Returns:
        requests.Session: A configured session to handle temporary API failures continuously.
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
    """Fetches expenses of a deputy from the Chamber of Deputies API for years 2023 to 2026, with automatic pagination.

    Args:
        id_deputado (int): The deputy's ID in the API.
        session (requests.Session | None): A configured session to handle temporary failures. If None, a new session is created.

    Returns:
        list: A list with all expense records.
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