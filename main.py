import json
import os
from colorama import Fore, init

init(autoreset=True)

FILE_NAME = "tasks.json"


# Load Tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


# Save Tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Load Existing Tasks
tasks = load_tasks()


# Add Task
def add_task():
    task = input(Fore.YELLOW + "\nEnter Task: ")

    if task.strip() == "":
        print(Fore.RED + "Task cannot be empty!")
        return

    tasks.append(task)
    save_tasks(tasks)

    print(Fore.GREEN + "Task Added Successfully!")


# View Tasks
def view_tasks():
    if not tasks:
        print(Fore.RED + "\nNo Tasks Available!\n")
        return

    print(Fore.CYAN + "\n========== YOUR TASKS ==========\n")

    for index, task in enumerate(tasks, start=1):
        print(Fore.CYAN + f"{index}. {task}")


# Update Task
def update_task():

    if not tasks:
        print(Fore.RED + "No Tasks Available!")
        return

    view_tasks()

    try:
        number = int(input(Fore.YELLOW + "\nEnter Task Number to Update: "))

        if 1 <= number <= len(tasks):

            new_task = input(Fore.YELLOW + "Enter New Task: ")

            tasks[number - 1] = new_task

            save_tasks(tasks)

            print(Fore.GREEN + "Task Updated Successfully!")

        else:
            print(Fore.RED + "Invalid Task Number!")

    except ValueError:
        print(Fore.RED + "Please Enter a Valid Number!")


# Delete Task
def delete_task():

    if not tasks:
        print(Fore.RED + "No Tasks Available!")
        return

    view_tasks()

    try:
        number = int(input(Fore.YELLOW + "\nEnter Task Number to Delete: "))

        if 1 <= number <= len(tasks):

            deleted_task = tasks.pop(number - 1)

            save_tasks(tasks)

            print(Fore.GREEN + f"'{deleted_task}' Deleted Successfully!")

        else:
            print(Fore.RED + "Invalid Task Number!")

    except ValueError:
        print(Fore.RED + "Please Enter a Valid Number!")


# Main Program
while True:

    print(Fore.MAGENTA + "\n=========================================")
    print(Fore.MAGENTA + "         TO-DO LIST APPLICATION")
    print(Fore.MAGENTA + "=========================================")

    print(Fore.WHITE + "1. Add Task")
    print(Fore.WHITE + "2. View Tasks")
    print(Fore.WHITE + "3. Update Task")
    print(Fore.WHITE + "4. Delete Task")
    print(Fore.WHITE + "5. Exit")

    choice = input(Fore.YELLOW + "\nEnter Your Choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print(Fore.BLUE + "\nThank You For Using To-Do List Application!")
        break

    else:
        print(Fore.RED + "\nInvalid Choice! Please Try Again.")