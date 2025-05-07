def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print ("\nSimple Calculator")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
    print ("5. Exit")

    choice = input ("Enter your choice (1-5): ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = add(a,b)
        print("\nThe sum of the 2 numbers are", result)

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = subtract(a,b)
        print("\nThe difference of the 2 numbers are", result)

    elif choice == "3":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = multiply(a,b)
        print("\nThe product of the 2 numbers are", result)

    elif choice == "4":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = divide(a,b)
        print("\nThe quotient of the 2 numbers are", result)
        
    elif choice == "5":
        print ("Thanks for using the calculator, Goodbye!")
        break 
    else:
        print("Invalid Choice, Please Try Again")
