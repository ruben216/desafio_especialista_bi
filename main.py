import persist_mysql
import pandas as pd

dados_2 = {
    'COLUNA1':['asd','dsa','asda','uyuy'],
    'COLUNA2':['123','1233','1','1233']
}

df = pd.DataFrame(dados_2)

persist_mysql.crud.create(df,'tabela')

dados = (persist_mysql.crud.read('coluna1'))

print(dados)
