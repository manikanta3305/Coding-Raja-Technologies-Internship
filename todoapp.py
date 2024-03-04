import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return {"tasks": []}

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks["tasks"].append({
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: "))
    if 0 <= task_index < len(tasks["tasks"]):
        del tasks["tasks"][task_index]
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

def complete_task(tasks):
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(tasks["tasks"]):
        tasks["tasks"][task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def display_tasks(tasks):
    if tasks["tasks"]:
        print("\nTask List:")
        for i, task in enumerate(tasks["tasks"]):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")
    else:
        print("No tasks found.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
