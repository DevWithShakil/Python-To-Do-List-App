def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return

    print("\n===== ALL TASKS =====")

    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Status: {task['status']}")
        print("--------------------")