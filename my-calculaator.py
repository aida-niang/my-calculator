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

def apply_operation(num1, num2, operator):
    """Applies the operation between two numbers."""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator in ['/', '÷']:
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    elif operator == "%":
        return num1 % num2

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
                result = apply_operation(number1, number2, operator)
                
                # Display the result
                print(f"Result: {number1} {operator} {number2} = {result}")
                
                # Save to history
                save_to_history(f"{number1} {operator} {number2} = {result}")
        
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
            
            # Save to history
            save_to_history(f"{operator}({base if operator == '**' else number}) = {result}")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Ask if the user wants to continue
        choice = input("Do you want to perform another scientific calculation? (yes/no): ").strip().lower()
        if choice == 'no':
            print("Exiting the Scientific Calculator. Goodbye!")
            break
        elif choice != 'yes':
            print("Invalid input. Please choose 'yes' or 'no'.")

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

            # Ask if the user wants to add more numbers
            while True:
                add_more = input("Do you want to add more numbers? (yes/no): ").strip().lower()
                if add_more == 'yes':
                    # Get the new operator and number
                    operator = get_operator("Enter the operator (+, -, *, ÷, %): ")
                    number = get_number("Enter the next number: ")
                    
                    # Append the operator and number to the lists
                    numbers.append(number)
                    operators.append(operator)
                    operations.append(f" {operator} {number}")
                elif add_more == 'no':
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")

            # Perform the calculation in order of precedence (multiplication/division first)
            while True:
                # Loop to handle multiplication/division first
                for i in range(len(operators)):
                    if operators[i] in ['*', '/', '÷', '%']:
                        result = apply_operation(numbers[i], numbers[i + 1], operators[i])
                        numbers[i + 1] = result
                        operators.pop(i)
                        numbers.pop(i)
                        
                        # Rebuild the operations string
                        operations = [f"{num} {op}" for num, op in zip(numbers, operators)]
                        operations.insert(0, str(numbers[0]))  # Make sure to add the first number at the start
                        break
                else:
                    break

            # Now process the remaining operations (addition/subtraction)
            result = numbers[0]
            for i in range(len(operators)):
                result = apply_operation(result, numbers[i + 1], operators[i])

            # Display the result with all operations
            operation_string = ' '.join(operations)  # Join the operations string properly
            print(f"Final result: {operation_string} = {result}")
            
            # Save to history
            save_to_history(f"{operation_string} = {result}")

            # Ask if the user wants to perform another multi-number calculation
            continue_choice = input("Do you want to perform another multi-number calculation? (yes/no): ").strip().lower()
            if continue_choice == 'no':
                print("Exiting the Multi-Number Calculator. Goodbye!")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

def save_to_history(operation):
    """Sauvegarde l'opération dans le fichier historique."""
    try:
        with open("calculator_history.txt", "a") as file:
            file.write(operation + "\n")
    except Exception as e:
        print(f"An error occurred while saving to history: {e}")

def read_history():
    """Lit et affiche l'historique des opérations."""
    try:
        with open("calculator_history.txt", "r") as file:
            history = file.readlines()
            if not history:
                print("No operations in history.")
            else:
                print("History of operations:")
                for line in history:
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found.")
    except Exception as e:
        print(f"An error occurred while reading history: {e}")

def clear_history():
    """Efface l'historique."""
    try:
        with open("calculator_history.txt", "w") as file:
            file.truncate(0)
        print("History cleared successfully.")
    except Exception as e:
        print(f"An error occurred while clearing history: {e}")

#Main Menu for options
def display_menu():
    print("\nWelcome to My Calculator!")
    print("\n=== Menu ===")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Multi-Number Calculator")
    print("4. View History")
    print("5. Clear History")
    print("6. Exit")
    
def main():
    """Main function to choose between basic, scientific, or multi-number calculators."""
    while True:
        display_menu()
        choice = input("Choose an option (1-6):").strip().lower()
        if choice == "1":
            basic_calculator()
        elif choice == "2":
            scientific_calculator()
        elif choice == "3":
            multi_number_calculator()
        elif choice == "4":
            read_history()  # Afficher l'historique
        elif choice == "5":
            clear_history()  # Effacer l'historique
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 'basic', 'scientific', 'multi-number', 'history', 'clear_history', or type 'exit' to quit.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl + C detected. Exiting the program safely. Goodbye!")
        main()
