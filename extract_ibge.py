import pandas as pd
import requests as rq
import json
import numpy as np

# Objetivo: criar uma função que retorna o objeto contendo dados extraídos da API

url = "https://servicodados.ibge.gov.br/api/v3/agregados/1705/localidades/N7|N6"

dados = rq.get(url).json()

df_dados_completos = pd.DataFrame(dados)

print(df_dados_completos)