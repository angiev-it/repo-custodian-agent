def get_tasks():
return ["Buy groceries", "Finish assignment", "Call dentist"]

def add_task(tasks, new_task):
tasks.append(new_task)
return tasks

if name == "main":
tasks = get_tasks()
print("Current tasks:", tasks)
