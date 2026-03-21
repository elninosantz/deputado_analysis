# Deputado Analysis

Pipeline de dados para coleta, tratamento e análise de despesas parlamentares da Câmara dos Deputados utilizando a [API de Dados Abertos](https://dadosabertos.camara.leg.br/).

> 🚧 Projeto em desenvolvimento — estrutura sujeita a alterações.

## Objetivo

Construir um pipeline ETL para analisar gastos da 57ª legislatura e gerar visualizações que permitam identificar padrões de despesas por deputado, partido e estado.

## Stack

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Polars](https://img.shields.io/badge/Polars-gray?logo=polars)
![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet)
![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-red?logo=streamlit)

## Progresso

- [x] Extração de dados dos deputados via API
- [x] Filtragem de deputados em exercício
- [x] Coleta completa de despesas parlamentares
- [x] Tratamento das despesas
- [x] Estruturação do pipeline ETL
- [ ] Análise exploratória
- [ ] Dashboard de visualização

## Estrutura

```
DEPUTADO_ANALYSIS/
├── src/
│   ├── extract/          # Requisições à API
│   ├── load/             # Carregamento dos dados
│   └── transform/        # Limpeza e tratamento
├── data/
│   └── raw/              # Dados brutos
├── docs/
│   └── architecture.md   # Documentação da arquitetura
├── notebooks/
│   └── view_deputados    # Análises exploratórias
├── app.py
├── main.py
└── pyproject.toml
```

## Como rodar

```bash
uv sync
uv run main.py
```

## Fonte de dados

[API de Dados Abertos da Câmara dos Deputados](https://dadosabertos.camara.leg.br/)