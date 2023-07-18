from airflow import Dag
from airflow.operators import PythonOperators, BashOperators 
from datetime import datetime  
import pathlib

default_args = {
  'owner' : 'julitays',
  'depends_on_past': False, 
  'start_date': datetime(2023, 18, 07),
  'retries': 0
}

dag = DAG('python_hello_world_dag',
          default_args = default_args,
          cutchup = False,
          schedule_interval = '00 20 * * *')

def hello():
  return print('hello, world')

t1 = PythonOperator(
  task_id = 'task_1',
  python_callable = hello,
  dag = dag )

