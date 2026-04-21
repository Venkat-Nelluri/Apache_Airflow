from airflow.sdk import dag,task

@dag
def Xcom_dag():
    @task
    def push_xcom():
        return "Hello from XComs!"

    @task
    def pull_xcom(xcom_value):
        print(f"Received XCom value: {xcom_value}")

    xcom_value = push_xcom()
    pull_xcom(xcom_value)

Xcom_dag()

