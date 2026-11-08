
def main():
    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. View Pending Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Add Task Feature")
        elif choice == "2":
            print("View Task Feature")
        elif choice == "3":
            print("Update Task Feature")
        elif choice == "4":
            print("Delete Task Feature")
        elif choice == "5":
            print("Complete Task Feature")
        elif choice == "6":
            print("Pending Task Feature")
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
