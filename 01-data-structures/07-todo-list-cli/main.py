def main():
    tasks = load_tasks()

    while True:
        print("\n")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("\n1) Add  2) Delete  3) Quit")
        try:
            choice = int(input("> ").strip())
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            delete_tasks(tasks)
        elif choice == 3:
            break
        else:
            print("Invalid input. Please try again.")


def add_tasks(tasks):
    task = input("Type in the new task> ").strip()
    if task == "":
        print("Invalid input.")
        return
    tasks.append(task)
    save_tasks(tasks)

def delete_tasks(tasks):
    try:
        deleted = int(input("Type in the number of the task you with to delete > ").strip()) - 1
    except ValueError:
        print("Invalid input. Please try again.")
        return

    if deleted >= len(tasks):
        print("Invalid input.")
        return
    del tasks[deleted-1]
    save_tasks(tasks)

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            content = f.read().strip()
            if content == "":
                return []
            return content.split("\n")
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    paste = "\n".join(tasks)
    with open('tasks.txt', 'w') as f:
        f.write(paste)



if __name__ == "__main__":
    main()