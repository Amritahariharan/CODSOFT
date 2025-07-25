import os
import datetime

TASK_FILE = "todo_tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        lines = file.readlines()
        tasks = [eval(line.strip()) for line in lines]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
        return
    print("\n📋 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{i}. [{status}] {task['task']} (Created: {task['created']})")

# Add a new task
def add_task(tasks):
    task_text = input("🆕 Enter the task: ").strip()
    if task_text:
        tasks.append({
            "task": task_text,
            "completed": False,
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print("✅ Task added successfully.")
    else:
        print("⚠️ Task cannot be empty.")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("✔️ Enter task number to mark as completed: "))
        if 0 < num <= len(tasks):
            tasks[num - 1]['completed'] = True
            print("🎉 Task marked as completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("🗑️ Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🧹 Task '{removed['task']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Enter a valid number.")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("✏️ Enter task number to update: "))
        if 0 < num <= len(tasks):
            new_text = input("🔄 Enter new task description: ").strip()
            if new_text:
                tasks[num - 1]['task'] = new_text
                print("✍️ Task updated.")
            else:
                print("⚠️ Task cannot be empty.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Enter a valid number.")

# Main Menu
def main():
    tasks = load_tasks()

    while True:
        print("\n====== 📝 TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("👉 Choose an option (1-6): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            update_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
