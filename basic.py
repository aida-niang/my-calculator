def get_number(prompt):
    """
    Function to get a valid number from the user.
    Args:
        prompt (str): The prompt message for input.
    Returns:
        float: The valid number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    """
    Function to get a valid operator from the user.
    Returns:
        str: The valid operator entered by the user.
    """
    while True:
        operator = input("Enter the operator (+, -, *, ÷(/), %): ").strip()
        if operator in ['+', '-', '*', '/', '÷', '%']:
            return operator
        print("Invalid operator. Please choose from: +, -, *, ÷(/), %.")

def basic_calculator():
    """
    Function to perform basic calculations (+, -, *, /, %).
    """
    print("\nWelcome to the Basic Calculator!")
    print("Available operators are: +, -, *, ÷(/), %")
    
    while True:
        try:
            # Get the first number
            number1 = get_number("Enter the first number: ")
            
            # Get the operator
            operator = get_operator()
            
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

def main():
    """
    Main function to run the Basic Calculator.
    """
    # Display a welcome message
    print("\nWelcome to the Basic Calculator!")
    print("Available operators are: +, -, *, ÷(/), %")
    
    # Start the calculator
    basic_calculator()

# Run the main program
if __name__ == "__main__":
    main()
