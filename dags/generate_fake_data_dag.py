from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.fake_data_generator import generate_and_insert_fake_data

with DAG(
    dag_id="fake_data_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["example"]
) as dag:
    generate_task = PythonOperator(
        task_id="generate_fake_data",
        python_callable=generate_and_insert_fake_data
    )




