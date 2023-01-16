from pandas import DataFrame
from pandas.io.json import json_normalize
import pandas as pd
import requests as rq
import json
import numpy as np
from numpy.lib.function_base import diff

# Objetivo: criar uma função que retorna o objeto contendo dados extraídos da API

url = "http://servicodados.ibge.gov.br/api/v3/agregados/2205/periodos/201001|201002|201003|201004|201101|201102|201103|201104|201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104/variaveis/1141?localidades=N1[all]&classificacao=12116[all]"

# Não precisa executar get, o read_json já faz isso :)
dados = rq.get(url).json()

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

dados_json = df.to_json()

print(dados_json)