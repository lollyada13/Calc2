# Function to perform arithmetic operations based on user input
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    elif operation == 'exponentiate':
        return num1 ** num2
    elif operation == 'modulus':
        if num2 == 0:
            return "Error! Modulus by zero."
        return num1 % num2
    else:
        return "Invalid operation"

# Main calculator loop

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. Quit")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        operation_dict = {
            '1': 'add',
            '2': 'subtract',
            '3': 'multiply',
            '4': 'divide',
            '5': 'exponentiate',
            '6': 'modulus'
        }
        operation = operation_dict[choice]

        num1 = input("Enter first number: ")
        num1_type = input("Enter type of first number (int/float): ")
        num1 = int(num1) if num1_type == "int" else float(num1)

        num2 = input("Enter second number: ")
        num2_type = input("Enter type of second number (int/float): ")
        num2 = int(num2) if num2_type == "int" else float(num2)

        print("Result:", perform_operation(num1, num2, operation))

    elif choice == '7':
        print("Thank you for using the calculator. Goodbye!")
        break
    else:
        print("Invalid input")