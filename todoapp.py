tasks = []

def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def delete_task(task_num):
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Deleted: {deleted_task}")
    else:
        print("Invalid task number.")

def complete_task(task_num):
    if 1 <= task_num <= len(tasks):
        completed_task = tasks[task_num - 1]
        tasks[task_num - 1] = f"[Completed] {completed_task}"
        print(f"Completed: {completed_task}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Complete task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            task_num = int(input("Enter the task number to delete: "))
            delete_task(task_num)
        elif choice == "4":
            task_num = int(input("Enter the task number to mark as complete: "))
            complete_task(task_num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
