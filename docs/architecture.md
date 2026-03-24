# ETL Deputados - Arquitetura do Projeto

## Regras de Negócio

> Para conhecer os desafios técnicos enfrentados durante o desenvolvimento do projeto, acesse: [Desafios Técnicos](desafios_tecnicos.md)

### Contexto

O objetivo do projeto é extrair, estruturar e analisar dados dos deputados com base nos **mandatos mais recentes**.

Para isso, a análise considera apenas os parlamentares pertencentes à **57ª legislatura**, que corresponde à legislatura atual no momento da coleta dos dados.

Como forma de contextualizar os dados analisados, também é exibida separadamente a **informação temporal da legislatura atual**, incluindo:

- número da legislatura
- data de início
- data de término

Essas informações servem como **referência temporal** para toda a análise.

### Evolução do objetivo analítico

Inicialmente, o foco do projeto era identificar **os 100 deputados que mais gastaram**.

Com a evolução da ideia, o escopo da análise foi ampliado para também:

- identificar **quais são as 5 maiores despesas** dos deputados analisados
- verificar **o gasto de cada deputado por ano**

Dessa forma, o projeto deixou de olhar apenas para o volume total de gastos e passou a considerar também a **composição** e a **distribuição temporal** dessas despesas.

---

## Uso dos Endpoints da API

O único endpoint que fornece a informação necessária para filtrar os deputados pela **situação do mandato** é:

`/deputados/{id}`

Como esse processo exige centenas de requisições, os dados coletados são **armazenados localmente em CSV**, evitando múltiplas consultas repetidas à API e reduzindo o risco de atingir limites de requisição.

---

## Situação do Deputado

Durante a etapa de limpeza dos dados, apenas deputados **em exercício** são considerados para análise.

Atualmente, um deputado pode apresentar as seguintes situações:

- **Licença**: deputado afastado temporariamente do cargo
- **Encerrado**: deputado que já deixou o cargo
- **Exercício**: deputado atualmente ativo no mandato
- **Vacância**: cargo não ocupado no momento da coleta dos dados

Para fins de análise, apenas registros com status **Exercício** são mantidos.

---

# Arquitetura do Pipeline

O projeto foi estruturado seguindo o padrão **ETL (Extract, Transform, Load)**.

---

## Extract

### 1. Consulta inicial de deputados

Foi realizada uma consulta ao endpoint:

`/deputados`

O objetivo foi obter as **informações iniciais dos deputados**, incluindo seus **IDs únicos**, que seriam utilizados nas consultas posteriores.

**Módulo responsável:** `api_deputados_id`

---

### 2. Coleta de dados detalhados dos deputados

Com os IDs obtidos anteriormente, foi realizada uma consulta ao endpoint:

`/deputados/{id}`

Esse endpoint retorna informações mais completas sobre cada deputado.

**Módulo responsável:** `api_deputados`

---

### 3. Coleta de informações da legislatura

Foi realizada uma consulta ao endpoint:

`/legislaturas/{id}`

O objetivo é obter informações sobre:

- número da legislatura
- data de início
- data de término

Essas informações servem como **referência temporal para a análise dos dados**.

**Módulo responsável:** `api_legislaturas`

---

### 4. Coleta de despesas parlamentares

As despesas dos deputados são coletadas através do endpoint:

`/deputados/{id}/despesas`

Essa consulta retorna os registros de gastos realizados pelos parlamentares.

**Módulo responsável:** `api_despesas_deputado`

---

## Transform

### 1. Limpeza dos IDs dos deputados

A partir dos dados retornados pelo endpoint `/deputados`, são extraídos os **IDs dos deputados**, que são armazenados em uma **lista** para utilização nas consultas seguintes.

**Módulo responsável:** `cleaning_deputados_id`

---

### 2. Limpeza dos dados dos deputados

A partir das informações detalhadas retornadas pelo endpoint `/deputados/{id}`, são extraídos apenas os dados relevantes para análise:

- id
- nome do deputado
- sigla do partido
- sigla do estado (UF)

Durante esse processo, são mantidos **apenas deputados em exercício**.

Esses dados são organizados em um **dicionário**, onde:

- a chave representa o **ID do deputado**
- o valor contém os atributos associados ao parlamentar

**Módulo responsável:** `cleaning_deputados`

---

### 3. Limpeza dos dados da legislatura

Os dados obtidos do endpoint `/legislaturas/{id}` são tratados para extrair:

- número da legislatura
- data de início
- data de término

Essas informações são utilizadas para gerar uma **string informativa**, que contextualiza temporalmente os dados analisados.

**Módulo responsável:** `cleaning_legislaturas`

---

### 4. Limpeza das despesas parlamentares

Diferentemente dos outros módulos, o tratamento das despesas exigiu duas etapas.

Primeiramente, foi necessário obter os **IDs dos deputados** a partir do arquivo CSV previamente salvo.

Essa estratégia foi adotada para evitar um grande número de requisições à API, o que poderia causar:

- aumento significativo do tempo de execução
- risco de atingir limites de requisição

O processo foi realizado da seguinte forma:

1. leitura do arquivo `deputados.csv`
2. extração da coluna contendo os **IDs dos deputados**
3. conversão desses IDs em uma **lista**
4. utilização dessa lista para realizar consultas à API de despesas

Após isso, os dados retornados pela API foram tratados para extrair:

- ano da despesa
- tipo da despesa
- valor líquido da despesa

Até o momento, esses dados ainda não foram convertidos para a estrutura final de armazenamento.

**Módulo responsável:** `cleaning_despesas`

---

## Load

### Armazenamento dos dados dos deputados

Após o tratamento, os dados estruturados no dicionário são convertidos para um **DataFrame**.

O DataFrame é então exportado para um arquivo CSV, utilizando **orientação por índice**, em que o índice representa o **ID do deputado**.

Esse arquivo é utilizado posteriormente para alimentar as próximas etapas do pipeline.

**Módulo responsável:** `save_csv_deputados`

---

# Objetivo do Projeto

O objetivo deste projeto é construir uma base de dados estruturada que permita analisar **os gastos dos deputados**, oferecendo maior transparência sobre:

- quais foram os **100 deputados que mais gastaram**
- quais são os **tipos de despesas mais frequentes**
- quanto foi direcionado para cada tipo de despesa
- quais são as **5 maiores despesas** dos deputados analisados
- como se distribuem os **gastos anuais de cada deputado**

Essas informações poderão ser utilizadas posteriormente para gerar **análises exploratórias, relatórios e dashboards interativos**.

"""