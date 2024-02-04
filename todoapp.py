tasks = []

def display_tasks_by_tag(tag):
    filtered_tasks = [task for task in tasks if tag in task['tags']]
    if not filtered_tasks:
        print(f"No tasks found with the tag '{tag}'.")
    else:
        print(f"Tasks with the tag '{tag}':")
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task['description']} [Tags: {', '.join(task['tags'])}]")

def add_task(task, tags=[]):
    tasks.append({"description": task, "tags": tags})
    print(f"Added: {task}")

def delete_task(task_num):
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Deleted: {deleted_task['description']}")
    else:
        print("Invalid task number.")

def complete_task(task_num):
    if 1 <= task_num <= len(tasks):
        completed_task = tasks[task_num - 1]
        tasks[task_num - 1] = {"description": f"[Completed] {completed_task['description']}", "tags": completed_task['tags']}
        print(f"Completed: {completed_task['description']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display all tasks")
        print("2. Display tasks by tag")
        print("3. Add task")
        print("4. Delete task")
        print("5. Complete task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks_by_tag("")
        elif choice == "2":
            tag = input("Enter the tag to filter tasks: ")
            display_tasks_by_tag(tag)
        elif choice == "3":
            task = input("Enter the task: ")
            tags = input("Enter tags (comma-separated, e.g., work,urgent): ").split(',')
            add_task(task, [tag.strip() for tag in tags])
        elif choice == "4":
            task_num = int(input("Enter the task number to delete: "))
            delete_task(task_num)
        elif choice == "5":
            task_num = int(input("Enter the task number to mark as complete: "))
            complete_task(task_num)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
