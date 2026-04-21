from airflow.sdk import dag,task

@dag
def bash_dag():

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
    def version():
        print("Version 2")

    @task.bash
    def bash_oper():
        return "echo abcdef"


    fisrt = first_task()
    second = second_task()
    third = third_task()
    bash = bash_oper()
  
    fisrt >> second >> third >> bash

bash_dag()


