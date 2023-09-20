import os
import json

#main function
def tasks():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t\t***********************************************')
    print('\t\t*      To do list Command line Application    *')
    print('\t\t***********************************************')

    print('\t\t\tAvailable choices:')
    print('\t\t\t\t1.Add Tasks')
    print('\t\t\t\t2.View Tasks')
   
    selected = int(input('Enter value the value of your choice:'))

    if selected == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        addTasks()
    elif selected == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        viewTasks()
    else:
        print('Invalid choice')
        print('Please enter 1 for the first option or 2 for the second option')
        tasks()
#load from json file
def loadfromjson(data):
    task_name = input('Please enter the task?\n')
    status = "not completed"
    new_task = {"task": task_name, "status": status}
    data.append(new_task)
    return data


#add tasks function
def addTasks():
    print('\t\t***********************************************')
    print('\t\t*                  Add Task                   *')
    print('\t\t***********************************************')
    
    file_path = "tasks.json"
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        if file_size > 0:
                with open("tasks.json","r") as json_file:
                    data = json.load(json_file)
                    loadfromjson(data)
                with open("tasks.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
        else:
            data = []
            loadfromjson(data)
            with open("tasks.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
    tasks()
#view task function
def viewTasks():
    print('\t\t***********************************************')
    print('\t\t*              All your Tasks                 *')
    print('\t\t***********************************************')

    #Load existing files from the JSON file or initilizing
    try:
        with open("tasks.json", "r") as json_file:
            tasks = json.load(json_file)
    except FileNotFoundError:
        print("File is empty")

    #show tasks
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Task: {task['task']}, Status: {task['status']}")


    #update tasks
    task_name = input("Enter the name of the task you want to update: ")

    for task in tasks:
        if task['task'] == task_name:
            new_status = input("Mark as completed? (yes or no): ")
            if new_status.lower() == "yes":
                task["status"] = "completed"
                print("Task marked as completed")
            elif new_status.lower() == "no":
                task["status"] = "not completed"
                print("Task marked as not completed")
            else:
               print(f"Task '{task_name}' not found.")

    #save the updated list
    with open("tasks.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)

tasks()
