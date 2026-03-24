from transform.slicing_transform_df import transform_nome_id, transform_id_partido, transform_id_uf
import polars as pl

def save_csv_nome_id():
    """ Salva os dados dos nomes e ids dos deputados em um arquivo CSV.

    Returns:
        None: A função não retorna nenhum valor, apenas salva o arquivo CSV.
    """
    df_nome_id = transform_nome_id()
    df_nome_id.write_csv('data/processed/nome_id.csv')


def save_csv_id_uf():
    """ Salva os dados dos ids e ufs dos deputados em um arquivo CSV.

    Returns:
        None: A função não retorna nenhum valor, apenas salva o arquivo CSV.
    """
    df_id_uf = transform_id_uf()
    df_id_uf.write_csv('data/processed/id_uf.csv')


def save_csv_id_partido():
    """ Salva os dados dos ids e partidos dos deputados em um arquivo CSV.

    Returns:
        None: A função não retorna nenhum valor, apenas salva o arquivo CSV.
    """
    df_id_partido = transform_id_partido()
    df_id_partido.write_csv('data/processed/id_partido.csv')