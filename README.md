# Desafio especialista em BI

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white" /> 
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />

## Objetivos
  * Conectar na base do IBGE e extrair dados de CNT.
      https://sidra.ibge.gov.br/home/pms/brasil
      https://servicodados.ibge.gov.br/api/docs/agregados?versao=3
      
  * Utilizando Python, limpar os dados e organizar em Dataframes.
  * Persistir os dados em uma base MySQL, utilizando container MySQL (docker).
  * Executar rotina utilizando Airflow.
  * Acessar e ler os dados no PowerBI.
  * No PowerBI, gerar os Dashboards.
  
```mermaid
flowchart LR
   IBGE --> Python --> MySQL --> Airflow --> CSVFile --> PowerBI
```
