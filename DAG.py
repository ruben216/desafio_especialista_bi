import airflow.utils.dates
import pandas as pd
import requests as rq
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator



# Exemplo de DAG vazia
# with DAG(
#     "dag_empty_test", start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
#     schedule="@daily", catchup=False
# ) as dag:
#     op = EmptyOperator(task_id="task")

# 1º Definimos as funções "callables"
def read_data(**kwargs):
    url = "http://servicodados.ibge.gov.br/api/v3/agregados/2205/periodos/201001|201002|201003|201004|201101|201102|201103|201104|201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104/variaveis/1141?localidades=N1[all]&classificacao=12116[all]"
    print('read web page!')

    # Não precisa executar get, o read_json já faz isso :)
    dados = rq.get(url).json()

    # Agrupar os dados em duas listas.
    cont = 0
    ls_classif = []  # Resultado final
    ls_series = []
    for i in dados[0]["resultados"]:
        ls_classif.append(dados[0]["resultados"][cont]["classificacoes"][0]["categoria"])
        ls_series.append(dados[0]["resultados"][cont]["series"][0]["serie"])
        cont += 1

    df = pd.DataFrame(ls_classif)

    zipped = list(zip(ls_classif, ls_series))
    df = pd.DataFrame(zipped, columns=["Categoria", "Serie"])

    dados_json = df.to_json()
    # Passar o df gerado para o contexto kwarg
    kwargs['ti'].xcom_push(key='df_read', value=dados_json)

def write_file(**kwargs):
    json = kwargs['ti'].xcom_pull(key='df_read')
    df = pd.read_json(json)
    print('write file!')
    df.to_csv('./arquivo_2_csv.csv')


# Config das DAGs

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(7)
}

pipeline = DAG("pipeline_dados", start_date=pendulum.datetime(2023, 1, 5, tz="UTC"),
               schedule_interval='*/5 * * * *', default_args=default_args, catchup=False)

read_data = PythonOperator(
    task_id='read_data_from_web',
    python_callable=read_data,
    dag=pipeline
)

write_file = PythonOperator(
    task_id='write_to_csv',
    python_callable=write_file,
    dag=pipeline
)

read_data >> write_file
