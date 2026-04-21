from airflow.sdk import dag,task
<<<<<<< HEAD
from airflow.operators.bash import BashOperator
=======

>>>>>>> e8504a1ea177ec28c14be2e199e7c12becd43279
@dag
def bash_dag():

    @task.python
    def first_task():
        print("hello World")

    
    @task.python
    def second_task():
        print("hello World2")
    
<<<<<<< HEAD
=======
    
    @task.python
    def third_task():
        print("hello World2")

    @task.python
    def version():
        print("Version 2")
>>>>>>> e8504a1ea177ec28c14be2e199e7c12becd43279

    @task.bash
    def bash_oper():
        return "echo abcdef"
<<<<<<< HEAD
    
    bah_task = BashOperator(
        task_id = "bash_task",
        bash_command = "echo Hello World"
    )

    fisrt = first_task()
    second = second_task()
    bash = bash_oper()
    bash_task = bah_task
  
    fisrt >> second >> bash >> bah_task
=======


    fisrt = first_task()
    second = second_task()
    third = third_task()
    bash = bash_oper()
  
    fisrt >> second >> third >> bash

>>>>>>> e8504a1ea177ec28c14be2e199e7c12becd43279
bash_dag()


