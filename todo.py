# todo.py

import os

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\n✅ Your to-do list is empty!")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("✅ Task added.")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"️ Removed: {removed}")
        else:
            print(" Invalid number.")
    except ValueError:
        print("️ Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print(" Tasks saved. Goodbye!")
            break
        else:
            print("️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
