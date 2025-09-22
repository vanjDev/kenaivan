tasks = []


def add_task(task):
    '''Adds a task to the task list.'''
    tasks.append(task)
    print("Task added!")


def show_tasks():
    '''Displays all tasks in the task list.'''
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("\nTasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])


def remove_task(task_number):
    '''Removes a task from the task list by its number.'''
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
        return
    tasks.pop(task_number - 1)
    print("Task removed!")


def border():
    '''Prints a border line.'''
    print("=" * 21)


def main():
    '''Prints the header'''
    border() 
    print("TODO List Application")
    border()

    # Main loop for the TODO list application.
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            border()
        elif choice == "2":
            show_tasks()
            border()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a number only!")
            border()
        elif choice == "4":
            print("Exiting...")
            border()
            break
        else:
            print("Wrong choice!")
            border()


if __name__ == "__main__":
    main()