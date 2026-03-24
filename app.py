from src.load.save_csv_slicing import save_csv_nome_id, save_csv_id_uf, save_csv_id_partido
from src.load.save_csv_valor_total_despesa import save_csv_os_mais_gastos_filtrados
from src.transform.cleaning_legislaturas import get_data_legislaturas
import webbrowser

import polars as pl

def legislatura():
    base_temporal_legislatura = get_data_legislaturas
    texto_encoded = urllib.parse.quote(base_temporal_legislatura)
    url = f"https://elninosantz.github.io/deputado_analysis/index.html?legislatura={texto_encoded}"
    webbrowser.open(url)

if __name__ == "__main__":
    legislatura()