from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

# Import your framework functions
from src.framework.etl_driver import run_pipeline


# 🔧 Default arguments
default_args = {
    "owner": "data_engineer",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}


# 🚀 DAG Definition
with DAG(
    dag_id="metadata_driven_etl",
    default_args=default_args,
    description="Metadata-driven ETL framework orchestration",
    schedule_interval="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["etl", "databricks", "metadata"]
) as dag:

    # 🧩 Pipeline list (can also come from config/db)
    pipelines = ["customer_etl", "orders_etl", "transactions_etl"]

    def run_pipeline_wrapper(pipeline_name):
        run_pipeline(pipeline_name)


    # 🔄 Dynamic Task Creation
    tasks = []

    for pipeline in pipelines:
        task = PythonOperator(
            task_id=f"run_{pipeline}",
            python_callable=run_pipeline_wrapper,
            op_kwargs={"pipeline_name": pipeline}
        )
        tasks.append(task)


    # 📊 Optional: Task Group for better UI
    with TaskGroup("etl_pipelines_group") as etl_group:
        for task in tasks:
            task


    # 🧭 Define execution order (parallel execution)
    etl_group
