import os

# File name for storing tasks
TASKS_FILE = 'tasks.txt'

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            for line in f:
                task_id, description, deadline, status = line.strip().split(',')
                tasks.append({
                    'id': int(task_id),
                    'description': description,
                    'deadline': deadline,
                    'status': status
                })
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            f.write(f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n")

# Function to add a task
def add_task(tasks):
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task_id = len(tasks) + 1  # Simple ID generation
    tasks.append({'id': task_id, 'description': description, 'deadline': deadline, 'status': 'Pending'})
    save_tasks(tasks)
    print("Task added successfully! (Task saved to tasks.txt)")

# Function to view tasks
def view_tasks(tasks):
    print("\nTo-Do List:")
    pending_tasks = [task for task in tasks if task['status'] == 'Pending']
    completed_tasks = [task for task in tasks if task['status'] == 'Completed']

    if pending_tasks:
        print("[Pending]")
        for task in pending_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("[Pending] No pending tasks.")

    if completed_tasks:
        print("\n[Completed]")
        for task in completed_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("[Completed] No tasks completed yet.")

# Function to edit a task
def edit_task(tasks):
    task_id = int(input("Enter task number to edit: "))
    for task in tasks:
        if task['id'] == task_id:
            new_description = input("Enter new task description: ")
            new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
            task['description'] = new_description
            task['deadline'] = new_deadline
            save_tasks(tasks)
            print("Task updated successfully! (Task status updated in tasks.txt)")
            return
    print("Task not found.")

# Function to delete a task
def delete_task(tasks):
    task_id = int(input("Enter task number to delete: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully! (Task removed from tasks.txt)")
            return
    print("Task not found.")

# Function to mark a task as completed
def complete_task(tasks):
    task_id = int(input("Enter task number to mark as completed: "))
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            save_tasks(tasks)
            print("Task marked as completed! (Task status updated in tasks.txt)")
            return
    print("Task not found.")

# Main menu function
def main_menu():
    tasks = load_tasks()
    while True:
        print("\nWelcome to To-Do List Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            print("Thank you for using the To-Do List Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the To-Do List application
if __name__ == "__main__":
    main_menu()