def format_task_list(tasks):
return "\n".join(f"- {task}" for task in tasks)

def count_tasks(tasks):
return len(tasks)
