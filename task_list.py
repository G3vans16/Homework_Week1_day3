tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# MVP
# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks
def get_uncompleted_tasks(task_list):
    uncompleted_tasks = []
    for task in task_list:
        if task["completed"] == False:
            uncompleted_tasks.append(task["description"])

    print(uncompleted_tasks)
            
# Print a list of completed tasks
def get_completed_tasks(task_list):
    completed_tasks = []
    for task in task_list:
        if task["completed"] == True:
            completed_tasks.append(task["description"])

    print(completed_tasks)

# Print a list of all task descriptions
def get_task_descriptions(task_list):
    task_descriptions = []
    for task in task_list:
        task_descriptions.append(task["description"])

    print(task_descriptions)


# Print a list of tasks where time_taken is at least a given time
def get_long_tasks(given_time, task_list):
    long_tasks = []
    for task in task_list:
        if task["time_taken"] >= given_time:
            long_tasks.append(task["description"])

    print(long_tasks)


# Print any task with a given description
def get_specific_task(given_task, task_list):
    for task in task_list:
        if task["description"] == given_task:
            print(task["description"])

# get_uncompleted_tasks(tasks)
# get_completed_tasks(tasks)
# get_task_descriptions(tasks)
# get_long_tasks(16, tasks)
# get_specific_task("Wash Dishes", tasks)

# EXTENSION
# Given a description update that task to mark it as complete.
def update_task(given_task, task_list):
    for task in task_list:
        if task["description"] == given_task:
            task["completed"] = True
            # print(task_list)

# Add a task to the list
def add_task( ,task_list)

# update_task("Wash Dishes", tasks)