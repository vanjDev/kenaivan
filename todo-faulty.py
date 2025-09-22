tasks=[]

def addtask(task):
    tasks.append(task)
    print("task added!")
    print("=" * 20)


def showTasks():
    if len(tasks) == 0 :
        print("no tasks yet")
        print("=" * 20)

    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        print("=" * 20)

def removetask(tasknumber):
    #fix off-by-one and invalid input
    if tasknumber < 1 or tasknumber > len(tasks):
        print("invalid task number!")
        return
    tasks.pop(tasknumber - 1)
    print("task removed!!")
    print("=" * 20)


def main():
    while True:
        print("=" * 20)
        print("Kenaivan's To-do List")
        print("=" * 20)
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4. Exit")
        # change the variable for more readability of code

        choice = input("enter choice : ")
        print("=" * 20)

        if choice== "1":
            task = input("enter task : ")
            addtask(task)
        elif choice == "2":
            showTasks()
        elif choice == "3":
            try:
                number = int(input("enter task no to remove: "))
                removetask(number)
            except ValueError:
                print("please enter a number only!")
        elif choice == "4":
            print("Program will now close")
            print("Thank you!")
            break
        else:
            print("wrong choice!!")
main()