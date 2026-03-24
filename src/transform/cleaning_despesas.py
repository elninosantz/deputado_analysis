from src.extract.api_despesas_deputados import fetch_despesas_deputados, create_session
import polars as pl
import time


def get_id_deputados() -> list[int]:
    """Reads deputy data from CSV and returns IDs as a list.

    Returns:
        list[int]: List of deputy IDs.
    """
    deputados = pl.read_csv('data/raw/deputados.csv')
    id_deputados = deputados['id'].to_list()
    
    return id_deputados


def get_data_despesas() -> dict[int, list[dict]]:
    """Extracts deputy expenses data using their IDs.

    Returns:
        dict[int, list[dict]]: Dictionary containing expense values, types, and years.
    """
    i = 1
    despesas_dos_deputados = {}
    id_deputados = get_id_deputados()
    session = create_session()
    total_deputados = len(id_deputados)

    for i, id_ in enumerate(id_deputados, 1):
        try:
            despesas_raw = fetch_despesas_deputados(id_, session=session)
            despesas_dos_deputados[id_] = [            
                {
                    'tipoDespesa': despesa['tipoDespesa'],
                    'valorLiquido': despesa['valorLiquido'],
                    'ano': despesa['ano']
                }
                for despesa in despesas_raw
                ]
            print(f"{i}/{total_deputados} — deputado {id_} extraído.", end="\r")
            time.sleep(35)
            
        except Exception as e:
            print(f"Erro ao extrair dados do deputado {id_}: {e}")
    return despesas_dos_deputados
