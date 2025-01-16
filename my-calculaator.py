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
    print("You can now enter a combination of numbers and operators.")
    
    while True:
        try:
            # Start by asking the user for the first number
            number1 = get_number("Enter the first number: ")

            # Get the first operator
            operator = get_operator("Enter the operator (+, -, *, ÷, %): ")

            # Get the second number
            number2 = get_number("Enter the second number: ")

            # Perform the first operation
            result = perform_operation(number1, number2, operator)

            print(f"Result so far: {number1} {operator} {number2} = {result}")
            
            # Continue asking for more numbers and operators
            while True:
                continue_calculation = input("Do you want to add another number? (yes/no): ").strip().lower()
                if continue_calculation == 'yes':
                    operator = get_operator("Enter the next operator (+, -, *, ÷, %): ")
                    number = get_number("Enter the next number: ")
                    result = perform_operation(result, number, operator)
                    print(f"Result so far: {result}")
                elif continue_calculation == 'no':
                    print(f"Final result: {result}")
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

def perform_operation(number1, number2, operator):
    """Perform the arithmetic operation between two numbers."""
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator in ['/', '÷']:
        if number2 == 0:
            raise ValueError("Cannot divide by zero.")
        return number1 / number2
    elif operator == "%":
        return number1 % number2

def main():
    """Main function to choose between basic, scientific, or multi-number calculators."""
    while True:
        print("\nWelcome to My Calculator!")
        choice = input("Select the type of calculator: basic, scientific, or multi-number (or type 'exit' to quit): ").strip().lower()
        
        if choice == "basic":
            basic_calculator()  # You would have this function implemented earlier
        elif choice == "scientific":
            scientific_calculator()  # You would have this function implemented earlier
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
