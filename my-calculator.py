from datetime import datetime
import locale

# Function 1 : test if the user enter a numeric value
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

###########################################################################################################
# Function 2 : test if the user enter a valid operator
def get_operator(prompt):
    while True:
        operator = input(prompt).strip()
        if operator in ['+', '-', 'x', '/', '÷', '%', 'sqrt', '√', 'x²', 'x2', 'sin', 'cos', 'tan', '**']:
            return operator
        print("Invalid operator. Please choose a valid operator.")

###########################################################################################################
# Function 3 : Create the 2-variables calculator
def apply_operation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "x":
        return num1 * num2
    elif operator in ['/', '÷']:
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    elif operator == "%":
        return num1 % num2

###########################################################################################################
# Function 4 : execute the 2-variables calculator
def basic_calculator():
    print("\nWelcome to the Basic Calculator!")
    print("Available operators are: +, -, x, ÷(/), %")
    
    while True:
        try:
            # Get the first number
            number1 = get_number("Enter the first number: ")
            
            # Get the operator
            operator = get_operator("Enter the operator (+, -, x, ÷(/), %): ")
            
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


###########################################################################################################
# Function 5 : execute the scientific calculator
def scientific_calculator():
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


###########################################################################################################
# Function 6 : execute the n-variables calculator

def multi_number_calculator():
    print("\nWelcome to the Multi-Number Calculator!")
    print("You must enter at least 3 numbers and 2 operators !")

    while True:
        try :
            operation = input("Enter your operation (please put space between each term): ")

            # Validate input
            terms = operation.split()
            if len(terms) < 5 or not all(term.isdigit() or term in ['+', '-', 'x', '/'] for term in terms):
                print("Invalid input. Please enter a valid operation.")
                continue

            def evaluate_operator(terms, operator):
                i = 0
                while i < len(terms):
                    if terms[i] == operator:
                        try:
                            if operator == 'x':
                                result = int(terms[i - 1]) * int(terms[i + 1])
                            elif operator == '/':
                                if int(terms[i + 1]) == 0:
                                    raise ZeroDivisionError("Division by zero is not allowed.")
                                result = int(terms[i - 1]) // int(terms[i + 1])
                            elif operator == '+':
                                result = int(terms[i - 1]) + int(terms[i + 1])
                            elif operator == '-':
                                result = int(terms[i - 1]) - int(terms[i + 1])

                            terms[i - 1] = str(result)
                            del terms[i:i + 2]
                            i -= 1
                        except Exception as e:
                            print(f"Error: {e}")
                            return None
                    else:
                        i += 1
                return terms

            for op in ['x', '/', '+', '-']:
                terms = evaluate_operator(terms, op)
                if terms is None:
                    break

            if terms is None:
                print("Calculation could not be completed due to an error.")
                continue

            result = terms[0]
            print(f"Result: {operation} = {result}")

            save_to_history(f"{operation} = {result}")

            # Ask for continuation
            continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice == 'no':
                print("Exiting the Multi-Number Calculator. Goodbye!")
                break
        except Exception as e:
            print(f"An error occurred: {e}")


###########################################################################################################
# Function 7 : Create and save the operation's history
def save_to_history(operation):
    try:
        # Set the locale to French (France)
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        
        # Get the current date and time in French format
        current_time = datetime.now().strftime("%A %d %B %Y à %H:%M:%S")
        
        # Create the string to save with the timestamp
        history_entry = f"{current_time} - {operation}"
        
        # Append the operation with timestamp to the history file
        with open("calculator_history.txt", "a") as file:
            file.write(history_entry + "\n")
    except Exception as e:
        print(f"An error occurred while saving to history: {e}")


###########################################################################################################
# Function 8 : Read the operation's history
def read_history():
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


###########################################################################################################
# Function 9 : Clear the operation's history 
def clear_history():
    try:
        with open("calculator_history.txt", "w") as file:
            file.truncate(0)
        print("History cleared successfully.")
    except Exception as e:
        print(f"An error occurred while clearing history: {e}")


###########################################################################################################
# Function 10 : Create a menu to make easy the manipulation of the calculator (for the user)
def display_menu(): 
    print("\nWelcome to My Calculator!")
    print("\n=== Menu ===")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Multi-Number Calculator")
    print("4. View History")
    print("5. Clear History")
    print("6. Exit")


###########################################################################################################
# Function 11 : Active the options depending on the user's choice   
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-6):").strip().lower()
        if choice == "1" or choice =='basic' or choice =='b':
            basic_calculator()
        elif choice == "2" or choice =='scientific' or choice =='s':
            scientific_calculator()
        elif choice == "3" or choice =='multi' or choice =='m':
            multi_number_calculator()
        elif choice == "4" or choice =='history' or choice =='h':
            read_history()  
        elif choice == "5" or choice =='clear' or choice =='c':
            while True:  # Boucle pour reposer la question en cas d'entrée invalide
                confirm = input("Do you really want to clear the history? (yes/no): ").strip().lower()
                if confirm == "yes":
                    clear_history()
                    break  # Sort de la boucle une fois l'action terminée
                elif confirm == "no":
                    print("History not cleared.")
                    break  # Sort de la boucle si l'utilisateur refuse de supprimer
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
        elif choice == "6" or choice == 'exit' or choice == 'e':
            print("Exiting the program safely. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 'basic', 'scientific', 'multi-number', 'history', 'clear_history', or type 'exit' to quit.")

# The main loop (to excecute and quit correctly the programm)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nReturning to the Menu ...")
        main()
