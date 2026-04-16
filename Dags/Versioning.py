from airflow.sdk import dag,task

@dag
def version_dag():

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

    @task.python
    def Version_2():
        print("new version")



    fisrt = first_task()
    second = second_task()
    third = third_task()
    vers = Version_2()

    fisrt >> second >> third >> vers

version_dag()


