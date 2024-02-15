import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

import logging

logging.basicConfig(level=logging.INFO)

default_args = {
    "owner": "Andrew McMahon",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "email": ["example@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}


def get_data():
    pass


def train_model():
    pass


def persist_model():
    pass


with DAG(
    dag_id="classification_pipeline",
    start_date=datetime.datetime(2024, 2, 14),
    schedule_interval="50 12 * * *",
    catchup=False,
) as dag:

    logging.info("DAG started ...")
    logging.info("Extracting and clustering data ...")
    get_data_task = PythonOperator(task_id="get_data", python_callable=get_data)

    logging.info("Extracting and summarizing data ...")
    train_model_task = PythonOperator(
        task_id="train_model", python_callable=train_model
    )

    logging.info("Persisting model ...")
    persist_model_task = PythonOperator(
        task_id="persist_model", python_callable=persist_model
    )

    get_data_task >> train_model_task >> persist_model_task


# #instantiate DAG
# dag = DAG(
#     'classification_pipeline',
#     default_args=default_args,
#     description="Basic pipeline for classifying the Wine Dataset",
#     schedule_interval=timedelta(days=1),
# )


# get_data = BashOperator(
#     task_id='get_data',
#     bash_command='python3 /usr/local/airflow/scripts/get_data.py',
#     dag=dag,
# )

# train_model= BashOperator(
#     task_id='train_model',
#     depends_on_past=False,
#     bash_command='python3 /usr/local/airflow/scripts/train_model.py',
#     retries=3,
#     dag=dag,
# )

# # Persist to MLFlow
# persist_model = BashOperator(
#     task_id='persist_model',
#     depends_on_past=False,
#     bash_command='python3 /usr/local/airflow/scripts/persist_model.py',
#     retries=3,
#     dag=dag,
# )

# get_data >> train_model >> persist_model
