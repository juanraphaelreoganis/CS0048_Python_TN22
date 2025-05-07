
def cel_to_fah():
    celsius = float(input("Enter temperature in Celsius: "))

    result = (celsius * (9/5)) + 32
    print("\nTemperature in Fahrenheit:", result)

def fah_to_cel():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    result = (fahrenheit - 32) * (5/9)
    print("\nTemperature in Celsius:", result)

while True:
    print ("\nMenu")
    print ("1. Convert Celsius to Fahrenheit")
    print ("2. Convert Fahrenheit to Celsius")
    print ("3. Exit")

    choice = input ("Enter your choice (1-3): ")

    if choice == "1":
        cel_to_fah()

    elif choice == "2":
        fah_to_cel()
        
    elif choice == "3":
        print ("Thanks for using the temperature converter, Goodbye!")
        break 
    else:
        print("Invalid Choice, Please Try Again")