
# Dataframe Deputados

### Contextos:
> Como o objetivo é extrair dados e compara-los de acordo com os utlimos mandados dos deputados, vamos trabalhar diretamente com os dados da 57 legislatura. 

- Nós vamos exebir separadamente o valor anual da legislatura atual para dar baseamento a analise. Não irei mostrar o inicio da exercção do mandato.

- O unico end-point que consigo pegar os dados que precisamos, ou o mais importante para o filtro
que é a situação, é o endpoint /deputado/{id}, como são centenas de requisições, vamos salvar os dados
em csv, para não consumir tanta requisição.

- Na parte de limpeza de dados, a gente vai utilizar as situações de deputados que estão exercendo
seu cargo, e sobre essas situações, atualmente um deputado pode ter as seguintes:
    - Licença: Afastado do Cargo
    - Encerrado: Saiu do cargo
    - Exercicio: Está ativo no cargo
    - Vecância: Não está ocupando o mandato no instante da coleta de dados
    
### Arquitetura:
**Extract Data**:
1. Extraimos os dados de ids, de todos os deputados do brasil através da api /deputados
2. Extraimos os dados de todos os deputados, com mais informações através da api /deputados/id

**Transform**:
1. Tratamos os dados, filtrando por legislatura(57) e situação(Exercicio).
2. Separamos os dados referentes a nome, uf de atuação, sigla partido, nome do deputado
3. Salvamos os dados em um dicionario

**Load**:
1. Abrimos os dados do dicionario e salvamos ele como CSV, com o objetivo de evitar estouro de
requisição.