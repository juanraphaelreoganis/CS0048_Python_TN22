import random

def checker():
    global rand_num
    global attempt_counter

    while True:
        chosen_rand = int(input("Guess the number (1-100): "))
        attempt_counter += 1
        if chosen_rand > rand_num:  
            print("Go lower!")
        elif chosen_rand < rand_num:
            print("Go Higher!")
        else:
            print("Congratulations! You guessed the number in", attempt_counter, "attempts!")
            break

while True:
    print("\nMenu")
    print("1. Play Number Guessing Game")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        rand_num = random.randint(1, 100)
        attempt_counter = 0
        checker()

    elif choice == "2":
        print("Thanks for playing the number guessing game, Goodbye!")
        break
    else:
        print("Invalid Choice, Please Try Again")