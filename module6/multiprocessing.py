import threading

class TaskRunner:
    def __init__(self, name):
        self.name = name

    def run_task(self, task_name):
        print(f"Running task: {task_name} on {self.name}")


task1 = TaskRunner("Task 1")
task2 = TaskRunner("Task 2")

thread1 = threading.Thread(target=task1.run_task, args=("Build",))
thread2 = threading.Thread(target=task2.run_task, args=("Deploy",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
