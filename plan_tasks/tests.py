from plan_tasks import *
tasks = [
    Task(4, 70),
    Task(2, 60),
    Task(4, 50),
    Task(3, 40),
    Task(1, 30),
    Task(4, 20),
    Task(6, 10)
]
print(tasks)
print("Naive:", naive_schedule(tasks))
print("Hitriy:", schedule_tasks(tasks))

tasks = [
    Task(3, 25),
    Task(4, 10),
    Task(1, 30),
    Task(3, 50),
    Task(3, 20)
]
print(tasks)
print("Naive:", naive_schedule(tasks))
print("Hitriy:", schedule_tasks(tasks))

