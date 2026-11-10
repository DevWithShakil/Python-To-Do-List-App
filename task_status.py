def complete_task(tasks):
    try:
        task_id = int(input("Enter Task ID to complete: "))
    except ValueError:
        print("Invalid ID!")
        return

    for task in tasks:
        if task["id"] == task_id:

            if task["status"] == "Completed":
                print("Task is already completed!")
                return

            task["status"] = "Completed"
            print("Task completed successfully!")
            return

    print("Task not found!")


def view_pending_tasks(tasks):
    pending_tasks = [
        task for task in tasks
        if task["status"] == "Pending"
    ]

    if not pending_tasks:
        print("No pending tasks!")
        return

    print("\n===== PENDING TASKS =====")

    for task in pending_tasks:
        print(
            f"ID: {task['id']} | "
            f"Title: {task['title']} | "
            f"Status: {task['status']}"
        )