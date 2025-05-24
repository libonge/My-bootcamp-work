# operation signs list for the programme
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
     return num1 / num2
# Open file
equations_file = open("equations.txt", "a")


while True:
    print("Menu:")
    print("1. Perform new calculations")
    print("2. Print previous equations from open text file")
    print("3. Exit")

    # Request user to choose an action from the menu
    choice = input("Enter your choice (1-3): ")

    # Choice 1 performs calculations
    if choice == "1":
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

        operation = input("Enter the operation (+, -, *, /): ")

        # Addition
        if operation == "+":
            result = num1 + num2
            print("Result:", result)
        # Subtraction
        elif operation == "-":
            result = num1 - num2
            print("Result:", result)
        # Multiplication
        elif operation == "*":
            result = num1 * num2
            print("Result:", result)
        # Division
        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero. Please try again.")
                continue
            result = num1 / num2
            print(result)
        else:
            print("Invalid operation. Please try again.")
            continue
        # Record the calculation in a text file
        with open('equations.txt', 'a') as file:
         file.write(f"{num1} {operation} {num2} = {result}\n")
       
    # Choice 2 prints previous calculations from the text file
    elif choice == "2":
        try:
            with open("equations.txt", "r") as file:
                equations = file.read()
                print("Previous Equations:")
                print(equations)
        except FileNotFoundError:
            print("No previous equations found.")

    # Choice 3 exits the program
    elif choice == "3":
        print("Exited")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 3.")