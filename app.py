from src.load.save_csv_slicing import save_csv_nome_id, save_csv_id_uf, save_csv_id_partido
from src.load.save_csv_valor_total_despesa import save_csv_valor_total_anos, save_csv_valor_total_despesa, save_csv_os_mais_gastos_filtrados
from src.transform.cleaning_legislaturas import get_data_legislaturas


import webbrowser
import urllib.parse

import polars as pl

def saves():
    """Saves various transformed data to CSV files.

    This function calls multiple saving functions to store different datasets in CSV format.
    Each saving function is responsible for a specific dataset, such as deputy information,
    expenses, and total expenses by year.

    Returns:
        None: The function does not return any value, it only saves the files.
    """
    save_csv_os_mais_gastos_filtrados()
    save_csv_nome_id()
    save_csv_id_uf()
    save_csv_id_partido()
    save_csv_valor_total_despesa()
    save_csv_valor_total_anos()

def legislatura():
    """Opens the web page with the current legislature information encoded in the URL.

    Retrieves the legislature data, encodes it, and opens the corresponding web page
    in the default browser with the legislature parameter.
    """
    base_temporal_legislatura = get_data_legislaturas()
    print(base_temporal_legislatura)
    texto_encoded = urllib.parse.quote(base_temporal_legislatura)
    url = f"https://elninosantz.github.io/deputado_analysis/index.html?legislatura={texto_encoded}"
    webbrowser.open(url)

if __name__ == "__main__":
    saves()
    legislatura()