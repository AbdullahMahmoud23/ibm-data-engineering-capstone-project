# Import the required libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Task 1 - Define the DAG arguments
default_args = {
    'owner': 'data_engineer',
    'start_date': days_ago(0),
    'email': ['businesselyamany@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Task 2 - Define the DAG
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='A daily DAG to extract, transform, and load web server log data',
    schedule_interval=timedelta(days=1), # Runs daily
)

# Task 3 - Create a task to extract data
# Assuming accesslog.txt is in the dags folder. 
# We use 'cut' to grab the first column (the IP address) based on space separation.
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d" " -f1 /opt/airflow/dags/accesslog.txt > /opt/airflow/dags/extracted_data.txt',
    dag=dag,
)

# Task 4 - Create a task to transform the data in the txt file
# We use 'grep -v' to filter OUT any line containing the specified IP address.
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v "198.46.149.143" /opt/airflow/dags/extracted_data.txt > /opt/airflow/dags/transformed_data.txt',
    dag=dag,
)

# Task 5 - Create a task to load the data
# We use 'tar' to archive the transformed file. 
# '-C /opt/airflow/dags' ensures we don't archive the entire folder path structure.
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cvf /opt/airflow/dags/weblog.tar -C /opt/airflow/dags transformed_data.txt',
    dag=dag,
)

# Task 6 - Define the task pipeline
extract_data >> transform_data >> load_data