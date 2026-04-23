from airflow.sdk import dag,task

@dag
def parallel_dag():

    @task.python
    def first_task():
        print("hello World")

    
    @task.python
    def second_task():
        print("hello World2")
    
    
    @task.python
    def third_task():
        print("hello World2")

    @task.python
    def fourth_task():
        print("hello World3")


    fisrt = first_task()
    second = second_task()
    third = third_task()
    fourth = fourth_task()

    fisrt >> [second, third] >> fourth


parallel_dag()


