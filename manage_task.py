def update_task(tasks):
    try:
        task_id = int(input("Enter Task ID to update: "))
    except ValueError:
        print("Invalid ID!")
        return

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new title: ").strip()

            if not new_title:
                print("Title cannot be empty!")
                return

            task["title"] = new_title
            print("Task updated successfully!")
            return

    print("Task not found!")


def delete_task(tasks):
    try:
        task_id = int(input("Enter Task ID to delete: "))
    except ValueError:
        print("Invalid ID!")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return

    print("Task not found!")