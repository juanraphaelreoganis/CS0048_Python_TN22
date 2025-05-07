tasks = []

def add_tasks():
    global tasks
    add = input("Enter the task to add: ")
    tasks.append(add)

def remove_tasks():
    global tasks
    remove = input("Enter the task to remove: ")
    tasks.remove(remove)
    
while True:

    print ("\nMenu")
    print ("1. Add Task")
    print ("2. Remove Task")
    print ("3. View Tasks")
    print ("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_tasks()
    elif choice == "2":
        remove_tasks()
    elif choice == "3":
        print("Tasks\n")
        print(*tasks, sep=', ')
    elif choice == "4":
        print ("Thanks for using the to-do list, Goodbye!")
        break 
    else:
        print("Invalid Choice, Please Try Again")