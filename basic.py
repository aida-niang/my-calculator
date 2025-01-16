
def basic_calculator():
    while True:
        try:
            # Get valid inputs
            number1 = get_number("Enter the first number: ")
            operator = get_operator(['+', '-', '*', '÷'])
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
            choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if choice == 'yes':
                break
            elif choice == 'no':
                print("Exiting the Basic Calculator. Goodbye!")
                return
            else:
                print("Invalid input. Please choose 'yes' or 'no'.")

def main():
    # Main function Basic calculator for arithmetic operations
    print("\nWelcome to the Basic Calculator!")
    print("Available operators are: +, -, *, ÷")
    basic_calculator()

# Run the main program
if __name__ == "__main__":
    main()
