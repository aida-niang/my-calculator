def get_number(prompt):  # to get a valid number from the user
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator(prompt):  # to get a valid operator from the user
    while True:
        operator = input(prompt).strip()
        if operator in ['+', '-', '*', '/', '÷', '%', '√', 'sqrt', 'x²', 'x2', 'sin', 'cos', 'tan', '**']:
            return operator
        print("Invalid operator. Please choose a available operator.")

def basic_calculator():
    # Start of the Basic Calculator function
    print("\nWelcome to the Basic Calculator!")
    print("Available operators are: +, -, *, ÷(/), %")
    
    while True:
        try:
            # Get the first number
            number1 = get_number("Enter the first number: ")
            
            # Get the operator
            operator = get_operator("Enter the operator (+, -, *, ÷(/), %): ")
            
            # Handle % operator separately
            if operator == '%':
                result = number1 / 100
                print(f"Result: {number1}% = {result}")
            else:
                # Get the second number
                number2 = get_number("Enter the second number: ")
                
                # Perform the operation
                if operator == '+':
                    result = number1 + number2
                elif operator == '-':
                    result = number1 - number2
                elif operator == '*':
                    result = number1 * number2
                elif operator in ['/', '÷']:
                    if number2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = number1 / number2
                
                # Display the result
                print(f"Result: {number1} {operator} {number2} = {result}")
        
        except Exception as e:
            # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")
        
        # Ask if the user wants to continue
        while True:
            choice = input("Do you want to perform another basic calculation? (yes/no): ").strip().lower()
            if choice == 'yes':
                break
            elif choice == 'no':
                print("Exiting the Basic Calculator. Goodbye!")
                return
            else:
                print("Invalid input. Please choose 'yes' or 'no'.")

def scientific_calculator():
    # Scientific calculator for advanced operations
    print("\nWelcome to the Scientific Calculator!")
    print("Available operators are: √ (square root), x² (square), sin, cos, tan, ** (power)")
    
    while True:
        try:
            # Get valid operator
            operator = get_operator("Enter the operator (√ (sqrt), x², sin, cos, tan, ** (power)): ")

            # Perform the selected operation
            if operator == "√" or operator == "sqrt":  
                number = get_number("Enter the number: ")
                if number < 0:
                    print("Square root of a negative number is not allowed.")
                    continue
                result = number ** 0.5
            elif operator == "x²" or operator == "x2":
                number = get_number("Enter the number: ")
                result = number ** 2
            elif operator == "sin" or operator == "cos" or operator == "tan":
                # Handle trigonometric functions
                degrees = get_number("Enter the angle in degrees: ")
                radians = degrees * (3.141592653589793 / 180)  # Convert degrees to radians
                
                if operator == "sin":
                    result = radians - (radians**3)/6 + (radians**5)/120
                elif operator == "cos":
                    result = 1 - (radians**2)/2 + (radians**4)/24
                elif operator == "tan":
                    result = (radians - (radians**3)/6 + (radians**5)/120) / (1 - (radians**2)/2 + (radians**4)/24)
            elif operator == "**":
                base = get_number("Enter the base: ")
                exponent = get_number("Enter the exponent: ")
                result = base ** exponent

            # Display the result
            print(f"Result: {result}")
        
        except Exception as e:
            # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")
        
        # Ask if the user wants to continue
        while True:
            choice = input("Do you want to perform another scientific calculation? (yes/no): ").strip().lower()
            if choice == 'yes':
                scientific_calculator()
            elif choice == 'no':
                print("Exiting the Scientist Calculator. Goodbye!")
                break  # Quitte la boucle pour terminer
            else:
                print("Invalid input. Please choose 'yes' or 'no'.")

def main():
    # Main function to choose between basic and scientific calculators
    while True:
        print("\nWelcome to My Calculator!")
        choice = input("Select the type of calculator: basic or scientific (or type 'exit' to quit): ").strip().lower()
        
        if choice == "basic":
            basic_calculator()
        elif choice == "scientific":
            scientific_calculator()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please select either 'basic', 'scientific', or type 'exit' to quit.")

# Run the main program
if __name__ == "__main__":
    main()
