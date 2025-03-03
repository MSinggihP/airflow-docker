from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    dag_id='first_sample_dag',
    start_date=datetime(2024, 5, 1),
    schedule_interval='00 11 * * 1',
    catchup=True
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    print_hello_world = BashOperator(
        task_id='print_hello_world',
        bash_command='python dags/modules/module1.py'
    )

    end_task = EmptyOperator(
        task_id='end'
    )

    test = EmptyOperator(
        task_id='test'
    )

start_task >> print_hello_world >> end_task