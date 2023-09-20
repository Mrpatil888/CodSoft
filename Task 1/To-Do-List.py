Str="\n To Do List"
print(Str.center(50))
# Initialize an empty list to store task_list
task_list=[]
# Function to add a task to the list
def add_task(task):
    task_list.append(task)
    print("Task",task,"added to the to-do-list")
# Function to remove a task from the list
def remove_task(task):
    if task in task_list:
        task_list.remove(task)
        print("Task",task,"removed from the to-do list.")
    else:
        print("Task",task," not found in the to-do list.")

# Function to update a task in the list
def update_task(old_task, new_task):
    if old_task in task_list:
        index = task_list.index(old_task)
        task_list[index] = new_task
        print(f"Task '{old_task}' has been updated to '{new_task}'.")
    else:
        print(f"Task '{old_task}' not found in the list.")

# Function to display the current to-do list
def display_task_list():
    if task_list:
        print("To-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(index,".",task)
    else:
        print("To-Do List is empty.")

# Main loop to interact with the to-do list
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display task_list")
    print("4. Update task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")
    match choice:
        case '1':
            task = input("Enter the task to add: ")
            add_task(task)
        case '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        case '3':
            display_task_list()
        case '4':
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            update_task(old_task, new_task)
        case '5':
            print("Goodbye!")
            exit(0)
        case _:
             print("Invalid choice. Please try again.")

        