from airflow.sdk import dag,task

@dag
def first_dag():

    @task.python
    def first_task():
        print("hello World")

    
    @task.python
    def second_task():
        print("hello World2")
    
    
    @task.python
    def third_task():
        print("hello World2")


    fisrt = first_task()
    second = second_task()
    third = third_task()

    fisrt >> second >> third

first_dag()


