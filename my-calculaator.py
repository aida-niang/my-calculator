def get_number(prompt):
    """Prompt the user to enter a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator(prompt):
    """Prompt the user to enter a valid operator."""
    while True:
        operator = input(prompt).strip()
        if operator in ['+', '-', '*', '/', '÷', '%']:
            return operator
        print("Invalid operator. Please choose a valid operator.")

def multi_number_calculator():
    """Multi-Number calculator function for multiple operations in one input."""
    print("\nWelcome to the Multi-Number Calculator!")
    print("You must enter at least 3 numbers and 2 operators.")
    
    while True:
        try:
            # Get the first number
            number1 = get_number("Enter the first number: ")
            numbers = [number1]
            operators = []
            operations = [str(number1)]

            # Get the first operator
            operator = get_operator("Enter the operator (+, -, *, ÷, %): ")
            operators.append(operator)

            # Get the second number
            number2 = get_number("Enter the second number: ")
            numbers.append(number2)
            operations.append(f" {operator} {number2}")

            # Get the second operator
            operator = get_operator("Enter the operator (+, -, *, ÷, %): ")
            operators.append(operator)

            # Get the third number (to ensure minimum 3 numbers)
            number3 = get_number("Enter the third number: ")
            numbers.append(number3)
            operations.append(f" {operator} {number3}")

            # Now that we have at least 3 numbers, let's start the calculation
            if operators[0] == "+":
                result = number1 + number2
            elif operators[0] == "-":
                result = number1 - number2
            elif operators[0] == "*":
                result = number1 * number2
            elif operators[0] in ['/', '÷']:
                if number2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = number1 / number2
            elif operators[0] == "%":
                result = number1 % number2

            print(f"Result so far: {result} {operators[0]} {number2}")

            # Perform the calculation after getting the third number
            if operators[1] == "+":
                result += number3
            elif operators[1] == "-":
                result -= number3
            elif operators[1] == "*":
                result *= number3
            elif operators[1] in ['/', '÷']:
                if number3 == 0:
                    raise ValueError("Cannot divide by zero.")
                result /= number3
            elif operators[1] == "%":
                result %= number3

            print(f"Result so far: {result} {operators[1]} {number3}")

            # Continue asking for more numbers and operators after the third one
            while True:
                continue_calculation = input("Do you want to add another number? (yes/no): ").strip().lower()
                if continue_calculation == 'yes':
                    operator = get_operator("Enter the next operator (+, -, *, ÷, %): ")
                    operators.append(operator)
                    number = get_number("Enter the next number: ")
                    numbers.append(number)
                    operations.append(f" {operator} {number}")
                    
                    # Perform the calculation after each new number and operator
                    if operator == "+":
                        result += number
                    elif operator == "-":
                        result -= number
                    elif operator == "*":
                        result *= number
                    elif operator in ['/', '÷']:
                        if number == 0:
                            raise ValueError("Cannot divide by zero.")
                        result /= number
                    elif operator == "%":
                        result %= number
                    print(f"Result so far: {result}")
                elif continue_calculation == 'no':
                    # Display the full expression
                    operation_string = ''.join(operations)
                    print(f"Final result: {operation_string} = {result}")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            
            # Ask the user if they want to perform another calculation
            continue_choice = input("Do you want to perform another multi-number calculation? (yes/no): ").strip().lower()
            if continue_choice == 'no':
                print("Exiting the Multi-Number Calculator. Goodbye!")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

def basic_calculator():
    """Basic Calculator function for simple arithmetic operations."""
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
                if operator == "+":
                    result = number1 + number2
                elif operator == "-":
                    result = number1 - number2
                elif operator == "*":
                    result = number1 * number2
                elif operator in ['/', '÷']:
                    if number2 == 0:
                        raise ValueError("Cannot divide by zero.")
                    result = number1 / number2
                elif operator == "%":
                    result = number1 % number2
                
                # Display the result
                print(f"Result: {number1} {operator} {number2} = {result}")
        
        except Exception as e:
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
    """Scientific Calculator function for advanced operations."""
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
            print(f"An unexpected error occurred: {e}")
        
        # Ask if the user wants to continue
        while True:
            choice = input("Do you want to perform another scientific calculation? (yes/no): ").strip().lower()
            if choice == 'yes':
                scientific_calculator()
            elif choice == 'no':
                print("Exiting the Scientist Calculator. Goodbye!")
                break  # Quit the loop to end
            else:
                print("Invalid input. Please choose 'yes' or 'no'.")

def main():
    """Main function to choose between basic, scientific, or multi-number calculators."""
    while True:
        print("\nWelcome to My Calculator!")
        choice = input("Select the type of calculator: basic, scientific, multi-number, or type 'exit' to quit: ").strip().lower()
        
        if choice == "basic":
            basic_calculator()
        elif choice == "scientific":
            scientific_calculator()
        elif choice == "multi-number":
            multi_number_calculator()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 'basic', 'scientific', 'multi-number', or type 'exit' to quit.")

# Run the main program
if __name__ == "__main__":
    main()
