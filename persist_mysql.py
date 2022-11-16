import mysql.connector
from mysql.connector import Error
import pandas as pd
import logging
from sqlalchemy import create_engine

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    filename='app.log',
    filemode='a'
)

mysql_conn = create_engine("mysql+mysqlconnector://root@172.17.0.2:3306/IBGE")

connection_config_dict = {
                'user' : 'root',
                'host' : '172.17.0.2',
                'port' : '3306',
                'database' : 'IBGE',
                'autocommit' : True
            }

class crud():
    def read (tabela):
        try:
            logging.debug('Iniciando conexão...')

            connection = mysql.connector.connect(**connection_config_dict)

            if connection.is_connected():
                db_Info = connection.get_server_info()
                logging.debug("Connected to MySQL Server version ", db_Info)
                # cursor = connection.cursor()
                # cursor.execute("select * FROM TESTE WHERE COLUNA1 = '123';")
                # record = cursor.fetchone()
                logging.debug("Guardando os dados da tabela em um objeto dataframe")
                dados = pd.read_sql_query("select * FROM TESTE",connection)
                connection.commit()
                return dados

        except Error as e:
            logging.ERROR("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                # cursor.close()
                connection.close()
                logging.debug("MySQL connection is closed")
    def create (dataframe,tabela):

        logging.debug('Iniciando conexão para persistir dados...')
        dataframe.to_sql(con=mysql_conn,name='TESTE',index=False,if_exists='append')







