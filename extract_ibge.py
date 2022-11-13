import pandas as pd
import requests
import json
import numpy as np

chave_portal = '6f98dcedb14a7c1053bc2bd8fb56ba5f'

# É necessário enviar a chave no Header da requisição
header_chave = {'chave-api-dados': chave_portal}

# Variavel que indica se tivemos conteúdo retornado do Portal
dados_pagina = "dados"

# Variável que controla a página que estamos iterando
pagina = 1

# Ano que iremos consultar
ano = 2021

# Objeto do tipo lista que irá armazenar os dados retornados de todas as páginas
dados_completos = []

# Laço que valida se o conteúdo retornado não está vazio.
while (dados_pagina):

    # A URL é montada informando o ano e a página
    url = f'http://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano={ano}&pagina={pagina}'

    # Neste ponto é enviada a request ao Portal de Transparencia, informando a URL e a chave.
    dados_pagina = requests.get(url, verify=True, headers=header_chave).json()

    # Caso tenha conteúdo no retorno, ele é adicionado ao objeto de dados_completos
    if (dados_pagina):
        dados_completos = dados_completos + dados_pagina
    pagina += 1

    # print(pagina)

df_dados_completos = pd.DataFrame(dados_completos)

df_dados_completos.head()