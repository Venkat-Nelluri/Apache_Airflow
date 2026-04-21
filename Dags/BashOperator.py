from airflow.sdk import dag,task
from airflow.operators.bash import BashOperator
@dag
def bash_dag():

    @task.python
    def first_task():
        print("hello World")

    
    @task.python
    def second_task():
        print("hello World2")
    

    @task.bash
    def bash_oper():
        return "echo abcdef"
    
    bah_task = BashOperator(
        task_id = "bash_task",
        bash_command = "echo Hello World"
    )

    fisrt = first_task()
    second = second_task()
    bash = bash_oper()
    bash_task = bah_task
  
    fisrt >> second >> bash >> bah_task
bash_dag()


