add_grade = 0
subject_count = 0 

def add_score():
    global add_grade
    global subject_count

    subject = input("Enter the subject: ")
    sub_grade = int(input("Enter the score: "))

    add_grade += sub_grade  
    subject_count += 1
    print("\nScore Added")

def average():
    global add_grade
    global subject_count

    if subject_count > 0:
        avg_grade = add_grade / subject_count
        print("Average Grade: ", avg_grade)
    else:
        print("No scores entered yet.")

while True:
    print("\nMenu")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_score()
    elif choice == "2":
        average()
    elif choice == "3":
        print("Thanks for using the student grade calculator, Goodbye!")
        break
    else:
        print("Invalid Choice, Please Try Again")
