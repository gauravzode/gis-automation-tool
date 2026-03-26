# todo_app.py

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            if not tasks:
                print("No tasks.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif choice == "2":
            task = input("New task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Added!")

        elif choice == "3":
            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)
                print("Deleted!")
            else:
                print("Invalid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")

    print("Goodbye!")

if __name__ == "__main__":
    main()


