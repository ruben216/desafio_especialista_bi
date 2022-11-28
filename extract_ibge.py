from pandas.io.json import json_normalize
import pandas as pd
import requests as rq
import json
import numpy as np
from numpy.lib.function_base import diff

# Objetivo: criar uma função que retorna o objeto contendo dados extraídos da API

url = "https://servicodados.ibge.gov.br/api/v3/agregados/2205/periodos/201001|201002|201003|201004|201101|201102|201103|201104|201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104/variaveis/1141?localidades=N1[all]&classificacao=12116[all]"

# Não precisa executar get, o read_json já faz isso :)
dados = rq.get(url).json()

df_categoria = dados[0]["resultados"][2]["classificacoes"][0]["categoria"]["101000"]

# Agrupar os dados em duas listas. 
cont = 0
ls_classif = [] # Resultado final
ls_series = []
for i in dados[0]["resultados"]:
  ls_classif.append(dados[0]["resultados"][cont]["classificacoes"][0]["categoria"])
  ls_series.append(dados[0]["resultados"][cont]["series"][0]["serie"])
  cont += 1

df = pd.DataFrame(ls_classif)


zipped = list(zip(ls_classif,ls_series))
df = pd.DataFrame(zipped,columns=["Categoria","Serie"])

# Explode a categoria
df2 = df.explode("Categoria")

# Explode a serie
df3 = df.explode("Serie")

def calc_series(row):
  a = row["Series_2"].get(row["Serie"])
  return a

def split_categ(row):
  a = row["Categoria"].get(row['Cod_Categoria'])
  return a

# Cria coluna auxiliar
df3["Series_2"] = df["Serie"]

# Reseta o index para permitir o get
df3 = df3.reset_index(drop=True)

# Aplica função lambda para criar coluna Valor
df3['Valor'] = df3.apply(lambda row: calc_series(row), axis=1)

# Cria coluna auxiliar
# df3["Cod_Categoria"] = df2["Categoria"]


# Aplica função lambda para criar coluna Nome
# df3['Nome_Categoria'] = df3.apply(lambda row: split_categ(row), axis=1)

print(df3)