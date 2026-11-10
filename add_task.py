def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty!")
        return

    next_id = max(
        (task["id"] for task in tasks),
        default=0
    ) + 1

    new_task = {
        "id": next_id,
        "title": title,
        "status": "Pending"
    }

    tasks.append(new_task)

    print("Task added successfully!")