import requests
import random

BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"
ANOS = "2023,2024,2025,2026"
HEADERS = {"accept": "application/json"}


def load_proxies(path: str = "proxies.txt") -> list:
    proxies = []
    with open(path) as f:
        for line in f:
            ip, porta, usuario, senha = line.strip().split(":")
            proxy_url = f"http://{usuario}:{senha}@{ip}:{porta}"
            proxies.append({"http": proxy_url, "https": proxy_url})
    return proxies


PROXIES = load_proxies()


def fetch_despesas_deputados(id_deputado: int) -> list:
    """Consulta despesas de um deputado da API da Câmara dos Deputados,
    dos anos 2023 até 2026, paginando automaticamente.

    :param id_deputado: ID do deputado na API.
    :return: Lista com todos os registros de despesas.
    """
    despesas = []
    pagina = 1

    while True:
        proxy = random.choice(PROXIES)
        response = requests.get(
            f"{BASE_URL}/deputados/{id_deputado}/despesas",
            headers=HEADERS,
            proxies=proxy,
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