import pickle


# Function to display the menu options
def display_menu():
    print("Todo List Manager")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("0. Exit")


# Function to add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")


# Function to mark a task as complete
def mark_task_complete(tasks):
    index = int(input("Enter the task index to mark as complete: "))
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task index.")


# Function to view the list of tasks
def view_tasks(tasks):
    print("Tasks:")
    for index, task in enumerate(tasks):
        status = "Complete" if task["completed"] else "Incomplete"
        print(f"{index}. {task['task']} - {status}")


# Function to delete a task
def delete_task(tasks):
    index = int(input("Enter the task index to delete: "))
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted.")
    else:
        print("Invalid task index.")


# Function to save tasks to a file
def save_tasks(tasks):
    file_name = input("Enter the file name to save tasks: ")
    with open(file_name, "wb") as file:
        pickle.dump(tasks, file)
    print("Tasks saved successfully.")


# Function to load tasks from a file
def load_tasks():
    file_name = input("Enter the file name to load tasks from: ")
    try:
        with open(file_name, "rb") as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully.")
        return tasks
    except FileNotFoundError:
        print("File not found.")
        return []


# Main function
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_complete(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
        elif choice == "6":
            tasks = load_tasks()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

        print()

    print("Thank you for using the Todo List Manager.")


# Run the program
if __name__ == "__main__":
    main()
