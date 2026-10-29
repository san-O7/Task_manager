import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("No saved tasks found. Starting fresh!")
        return []

taskList = load_tasks()

def taskManager():
    print("1. View tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Change priority")
    print("6. Exit")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(taskList, file, indent=4)

def view_tasks():
        if len(taskList) == 0:
                        print("You have no tasks")
        else:
            for index, task in enumerate(taskList, start=1):
                    print(f"{index}) [{task['priority']}] {task['title']}")
                    print("-----------------------------------------------")

def add_task():
        task = {}
        title = input("Add task: ").strip()
        if not title:
                print("Task title cannot be empty!")
                return
        priority = input("Choose priority (High/Medium/Low): ").capitalize()
        if priority not in ["High", "Medium", "Low"]:
                print("Invalid priority!")
                return
        task["title"] = title
        task["priority"] = priority
        taskList.append(task)
        save_tasks()
        print("Task added succesfully")

def delete_task():
    try:
        choice = int(input("Which task to delete: ")) - 1
    except ValueError:
           print("Invalid input!")
    
    if 0 <= choice < len(taskList):
        taskList.pop(choice)
        save_tasks()
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def edit_task():
        try:
                choice = int(input("Which task to edit? ")) - 1
        except ValueError:
                   print("Invalid input!")

        if 0 <= choice < len(taskList):
                new_title = input("Rewrite existing task: ").strip()

                if not new_title:
                        print("Task title cannot be empty!")
                        return

                taskList[choice]["title"] = new_title
                save_tasks()
                print("Task updated successfully!")

        else:
                print("Invalid task number!")

def change_priority():
    choice = int(input("Which task priority to change: ")) - 1

    if 0 <= choice < len(taskList):
        new_priority = input(
            "Select new priority (High/Medium/Low): "
        ).strip().capitalize()

        if not new_priority:
                print("Task priority cannot be empty!")
                return

        if new_priority not in ["High", "Medium", "Low"]:
                print("Invalid priority!")
                return

        taskList[choice]["priority"] = new_priority
        save_tasks()
        print("Priority changed succesfully")

    else:
        print("Invalid task number!")
        

    
while True:
    taskManager()

    choice = input("Choose an option: ").strip()

    if choice == 1:
        print("Selected view tasks")
        view_tasks()

    elif choice == 2:
            print("Selected add task")
            add_task()

    elif choice == 3:
            print("Selected Edit task")
            edit_task()

    elif choice == 4:
                print("Selected delete task")
                delete_task()

    elif choice == 5:
                print("Selected change priority")
                change_priority()
    elif choice == 6:
                print("Goodbye")
                break
    else:
            print("invalid input, try again!")




