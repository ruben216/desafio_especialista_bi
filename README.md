# Desafio especialista em BI

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white" /> 
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />

## Objetivos
  * Conectar na base do IBGE e extrair dados de CNT.
      https://sidra.ibge.gov.br/home/pms/brasil
      https://servicodados.ibge.gov.br/api/docs/agregados?versao=3
      Gráfico 1 – Exibir gráfico em linha com a evolução das contas CNTs tri a tri (posicionar a esquerda em cima)
      Deve conter o índice CNT em formato de gráfico em barra e deve contar linha de evolução Tri vs. Tri no mesmo gráfico
      Deve contar com filtro de data, início e fim do período escolhido.
      CNT = Contas Nacionais Trimestrais

  * Utilizando Python, limpar os dados e organizar em Dataframes.
  * Persistir os dados em uma base MySQL, utilizando container MySQL (docker).
  * Executar rotina utilizando Airflow.
  * Acessar e ler os dados no PowerBI.
  * No PowerBI, gerar os Dashboards.
  
## Dúvidas 

* CNT seriam as Contas Nacionais Trimestrais?
*  


```mermaid
flowchart LR
   IBGE --> Python --> MySQL --> Airflow --> CSVFile --> PowerBI
```
