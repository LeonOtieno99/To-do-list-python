import os
import json

print('\t\t\t***********************************************')
print('\t\t\t*      To do list Command line Application    *')
print('\t\t\t***********************************************')

def tasks():
    print('\t\t\t\tAvailable choices:')
    print('\t\t\t\t\t1.View Tasks')
    print('\t\t\t\t\t2.Add Tasks')
    selected = int(input('Enter value the value of your choice:'))

    if selected == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        viewTasks()
    elif selected == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        addTasks()
    else:
        print('Invalid choice')
        print('Please enter 1 for the first option or 2 for the second option')
        tasks()


def addTasks():
    print('\t\t\t***********************************************')
    print('\t\t\t*                  Add Task                   *')
    print('\t\t\t***********************************************')
    task_name = input('Please enter the task?\n')
    status = "not completed"
    new_task = {"task": task_name, "status": status}
    with open("tasks.json", "a+") as json_file:
        json.dump(new_task, json_file, indent=4)
        json_file.write("\n")

def viewTasks():
    print('\t\t\t***********************************************')
    print('\t\t\t*              All your Tasks                 *')
    print('\t\t\t***********************************************')

    #Load existing files from the JSON file or initilizing
    try:
        with open("tasks.json", "r") as json_file:
            tasks = json.load(json_file)
    except FileNotFoundError:
        tasks = []

    #show tasks
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Task: {task['task']}, Status: {task['status']}")


    #update tasks
    task_name = input("Enter the name of the task you want to update: ")

    for task in tasks:
        if task["task"] == task_name:
            new_status = input("Mark as completed? (yes or no): ")
            if new_status.lower() == "yes":
                task["status"] = "completed"
            elif new_status.lower() == "no":
                task["status"] = "not completed"
            else:
                print("invalid choice")
                break
        else:
            print(f"Task '{task_name}' not found.")

    #save the updated list
    with open("tasks.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)

    print("Goodbye!")


tasks()
