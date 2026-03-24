# 📊 Deputado Analysis - [Deploy](https://elninosantz.github.io/deputado_analysis/)

> Análise transparente e acessível dos gastos parlamentares da 57ª Legislatura

Uma plataforma completa para extrair, estruturar e analisar dados de despesas parlamentares da Câmara dos Deputados, transformando dados públicos em informações visuais e compreensíveis.

![Dashboard Preview](src/imgs/Captura%20de%20tela%202026-03-23%20234419.png)

## 🎯 Objetivo

Construir um **pipeline ETL robusto** que coleta, processa e visualiza os gastos da Cota para Exercício da Atividade Parlamentar (CEAP) dos deputados em exercício, identificando padrões de despesas por região, partido e período temporal.

## 🔍 Funcionalidades Principais

- ✅ Identificação dos **100 deputados com maiores gastos**
- ✅ Análise das **5 maiores categorias de despesa** por deputado
- ✅ Distribuição de gastos **por região e estado**
- ✅ Análise comparativa **por partido político**
- ✅ Evolução temporal dos gastos **por ano**
- ✅ Dashboard interativo com **visualizações em tempo real**

## 🛠️ Stack Tecnológico

### Backend & Data Processing
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Polars](https://img.shields.io/badge/Polars-cd5c5c?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHJ4PSI0IiBmaWxsPSIjRkZGRkZGIi8+PC9zdmc+&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.31+-61DAFB?logo=python)

### Frontend & Visualização
![HTML5](https://img.shields.io/badge/HTML5-E34C26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![PapaParse](https://img.shields.io/badge/PapaParse-CSV-red)

### DevOps & Gerenciamento
![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)

## 📦 Dependências Python

```toml
requests = "2.31+"           # Requisições HTTP para API
polars = "*"                 # Processamento de dados em alta performance
```

## 🏗️ Arquitetura

O projeto segue o padrão **ETL (Extract, Transform, Load)**:

```
┌─────────────────────────────────────────────────────────┐
│                      API CÂMARA                          │
│          (Dados Abertos Parlamentares)                   │
└────────────────┬────────────────────────────────────────┘
                 │
         ┌───────▼────────┐
         │    EXTRACT     │
         ├────────────────┤
         │ • Deputados    │
         │ • Despesas     │
         │ • Legislaturas │
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │   TRANSFORM    │
         ├────────────────┤
         │ • Limpeza      │
         │ • Filtragem    │
         │ • Agregação    │
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │      LOAD      │
         ├────────────────┤
         │ • CSV Files    │
         │ • GitHub Raw   │
         └───────┬────────┘
                 │
         ┌───────▼────────────────┐
         │   VISUALIZAÇÃO         │
         ├────────────────────────┤
         │ • Dashboard Web        │
         │ • Gráficos interativos │
         └────────────────────────┘
```

### Etapas do Pipeline

#### 🔸 Extract
- **API Deputados**: Coleta de IDs e dados detalhados dos parlamentares
- **API Despesas**: Extração de gastos parlamentares com paginação automática
- **API Legislaturas**: Contexto temporal da análise
- **Retry automático**: Tratamento robusto de falhas com backoff exponencial

#### 🔹 Transform
- **Filtragem**: Mantém apenas deputados em exercício
- **Normalização**: Extração de campos relevantes (ID, nome, partido, UF)
- **Agregação**: Cálculo de totais e rankings
- **Análise temporal**: Distribuição de gastos por ano

#### 🔸 Load
- **Armazenamento local**: CSV para análises futuras
- **GitHub Pages**: Publicação em repositório para acesso remoto
- **Estrutura hierárquica**: Dados brutos e processados separados

## 📁 Estrutura do Projeto

```
deputado_analysis/
├── 📂 src/
│   ├── 📂 extract/
│   │   ├── api_deputados.py              # Dados detalhados dos deputados
│   │   ├── api_despesas_deputados.py     # Gastos parlamentares com retry
│   │   ├── api_id_deputados.py           # IDs dos deputados
│   │   ├── api_legislaturas.py           # Informações da legislatura
│   │   ├── csv_deputados.py              # Leitura de CSVs
│   │   └── csv_despesas_deputados.py     # Leitura de despesas
│   │
│   ├── 📂 transform/
│   │   ├── cleaning_deputados.py         # Filtragem e normalização
│   │   ├── cleaning_deputados_id.py      # Extração de IDs
│   │   ├── cleaning_despesas.py          # Tratamento de despesas
│   │   ├── cleaning_legislaturas.py      # Contexto temporal
│   │   ├── os_maiores_gastos.py          # Ranking de despesas
│   │   ├── slicing_transform_df.py       # Slicing por região/partido
│   │   └── transform_valortotal_despesas.py  # Agregações
│   │
│   └── 📂 load/
│       ├── save_csv_deputados.py         # Persistência de deputados
│       ├── save_csv_despesas.py          # Persistência de despesas
│       ├── save_csv_slicing.py           # Persistência de slices
│       └── save_csv_valor_total_despesa.py  # Persistência de agregados
│
├── 📂 data/
│   ├── 📂 raw/                           # Dados brutos da API
│   │   ├── deputados.csv
│   │   ├── despesas_deputados.csv
│   │   └── maiores_gastos.csv
│   │
│   └── 📂 processed/                     # Dados tratados
│       ├── nome_id.csv
│       ├── id_uf.csv
│       ├── id_partido.csv
│       ├── valor_total_despesa.csv
│       ├── valor_total_por_ano.csv
│       └── maiores_gastos_filtrados.csv
│
├── 📂 docs/
│   ├── architecture.md                   # Documentação da arquitetura
│   ├── desafios_tecnicos.md             # Desafios encontrados
│   └── oq_fiz_de_novo.md                # Melhorias implementadas
│
├── 📂 notebooks/
│   └── view_deputados.ipynb              # Análises exploratórias
│
├── index.html                            # Dashboard web interativo
├── app.py                                # Script de inicialização
├── pyproject.toml                        # Configuração do projeto
└── README.md                             # Este arquivo
```

## 🎓 Regras de Negócio

### Escopo Temporal
- **Legislatura analisada**: 57ª Legislatura (2023-2027)
- **Filtro de situação**: Apenas deputados em **exercício**
- **Contexto temporal**: Exibição automática do período legislativo

### Análise de Dados
- **Top 100**: Ranking completo para análise contextual
- **Top 5**: Maiores categorias de despesa por deputado
- **Periodicidade**: Agregação de gastos por ano legislativo

### Tratamento de Falhas
- **Retry automático**: Até 5 tentativas em caso de erro
- **Backoff exponencial**: Aguardo progressivo entre tentativas
- **Logs detalhados**: Rastreamento de todas as operações

## 🚀 Como Usar

### Pré-requisitos
- Python 3.12+
- `uv` - Para gerenciamento de dependências

### Instalação

```bash
# Clonar repositório
git clone https://github.com/elninosantz/deputado_analysis.git
cd deputado_analysis

# Instalar dependências
uv sync

# Usar o ambiente virtual
uv run python app.py
```

### Executar o Pipeline

```bash
# Executar aplicação completa
uv run app.py

# Ou executar via terminal
python app.py
```

### Visualizar Dashboard

O dashboard web estará disponível em:
```
https://elninosantz.github.io/deputado_analysis/
```

## 📊 Dados Disponibilizados

### Dimensões de Análise

| Dimensão | Descrição | Arquivo |
|----------|-----------|---------|
| **Deputados** | ID, nome civil, UF, partido | `nome_id.csv`, `id_uf.csv`, `id_partido.csv` |
| **Gastos Totais** | Total por deputado, ranking | `valor_total_despesa.csv` |
| **Gastos Temporais** | Evolução anual de gastos | `valor_total_por_ano.csv` |
| **Categorias** | Top 5 despesas por tipo | `maiores_gastos_filtrados.csv` |

### Endpoints da API Utilizados

- `GET /deputados` - Lista de deputados da legislatura
- `GET /deputados/{id}` - Detalhes específicos do deputado
- `GET /deputados/{id}/despesas` - Despesas com paginação automática
- `GET /legislaturas/{id}` - Informações da legislatura

## 📈 Progresso

- [x] Extração de dados dos deputados via API
- [x] Coleta de despesas com paginação automática
- [x] Filtragem de deputados em exercício
- [x] Tratamento e normalização dos dados
- [x] Estruturação do pipeline ETL completo
- [x] Agregações e cálculos de rankings
- [x] Dashboard web interativo (GitHub Pages)
- [x] Melhorias de docstrings (Google Style)
- [ ] Análise exploratória avançada
- [ ] Dashboards adicionais (Streamlit)
- [ ] Testes automatizados

## 🔗 Fonte de Dados

**API de Dados Abertos da Câmara dos Deputados**

Documentação: https://dadosabertos.camara.leg.br/

- Endpoint base: `https://dadosabertos.camara.leg.br/api/v2`
- Taxa de limite: Requisições responsáveis com retry automático
- Formatos suportados: JSON, CSV

## 📚 Documentação Adicional

- [Arquitetura Detalhada](docs/architecture.md) - Descrição técnica do pipeline ETL
- [Desafios Técnicos](docs/desafios_tecnicos.md) - Problemas resolvidos e soluções
- [Melhorias Implementadas](docs/oq_fiz_de_novo.md) - Histórico de atualizações

## 🤝 Inspiração

Este projeto foi inspirado no excelente trabalho do projeto **[Olho Cidadão](https://github.com/brasilemdados/Olho-Cidadao)**, com a missão de ampliar a transparência e facilitar o acesso da população às informações sobre o uso de recursos públicos pelos deputados.

## 📝 Licença

Este projeto é de código aberto e disponível para fins educacionais e de pesquisa.

## 📧 Contato

**Autor**: Augusto Cesar  
**Email**: tiaugustocesar@gmail.com  
**Repositório**: https://github.com/elninosantz/deputado_analysis

---

<div align="center">

**Transformando dados públicos em informação acessível** 🇧🇷

Desenvolvido com ❤️ para transparência parlamentar

</div>
