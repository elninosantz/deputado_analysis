# Desafios Técnicos

## Limite de Requisição
Durante o desenvolvimento do projeto, foi identificado um problema relacionado ao grande volume de requisições e ao possível **limite de uso da API**.

### Uso inicial de proxies

Em um primeiro momento, foi adotada uma estratégia com uso de **proxies** para distribuir as requisições e reduzir a repetição de chamadas a partir de um mesmo endereço IP.

Para isso, foi utilizada a biblioteca `random`, responsável por selecionar os proxies de forma aleatória a cada requisição.

As proxies utilizadas foram obtidas na plataforma [Webshare](http://webshare.io/).

No entanto, como o projeto não possui recursos financeiros para contratação de serviços pagos e, por questões de segurança, não foi considerada a utilização de proxies públicos, essa estratégia se tornou limitada após o esgotamento das proxies gratuitas disponíveis.

### Substituição de Pandas por Polars

No início do projeto, o processamento dos dados estava sendo realizado com **Pandas**.

Posteriormente, após uma sugestão de um colega da área que atua como engenheiro de dados, foi realizada a migração para **Polars**, com o objetivo de melhorar o desempenho do processamento.

Essa mudança foi motivada pelo fato de o **Polars** apresentar melhor performance em operações de processamento de dados, especialmente em cenários com maior volume de informação.

Após a substituição, foi possível perceber uma melhoria no desempenho geral da etapa de transformação dos dados.

### Estratégia de resiliência para requisições

Diante da limitação no uso de proxies, a alternativa adotada foi tornar o processo de requisição mais resiliente e menos agressivo para a API.

Para isso, foi implementada uma função responsável por criar uma **sessão configurada com tentativas automáticas de repetição** em caso de falha temporária na API.

Essa sessão foi configurada com:

- total de **5 tentativas**
- repetição automática para os códigos de resposta **429, 502, 503 e 504**
- tempo de espera progressivo entre as tentativas

Para essa estratégia, foram utilizadas as bibliotecas `requests` e `urllib3`, com uso de `Retry` e `HTTPAdapter`.

O `HTTPAdapter` foi utilizado para aplicar à sessão a política de tentativas previamente configurada, permitindo maior tolerância a falhas momentâneas de conexão e indisponibilidade temporária da API.

Essa implementação pode ser observada no módulo `api_despesas_deputado`, na função `create_session`.

Além disso, cada requisição passou a utilizar um **timeout de 220 segundos**, como forma de reduzir falhas por encerramento prematuro da conexão em operações mais demoradas.

### Redução da agressividade nas coletas

Como medida adicional para reduzir a pressão sobre a API, durante a etapa final de extração e limpeza dos dados foi adotado um intervalo de espera entre as requisições.

No módulo `cleaning_despesas`, a sessão configurada pela função `create_session` é importada e reutilizada no processo de coleta.

Ao final da requisição de cada ID de deputado, foi adicionado um `sleep` de **35 segundos** antes da próxima chamada.

Essa abordagem tornou o processo mais lento, porém também mais estável, mais respeitoso com os limites da API e menos agressivo do que a estratégia inicialmente utilizada.