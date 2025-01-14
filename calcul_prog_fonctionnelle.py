#import the necessary libraries :
import numpy as np
import matplotlib.pyplot as plt



########################################################################
#define the functions :
# 1 - Define a basic calculator with basic operators : +, x,
def basic_calculator(a, b, operator) :
    if operator == '+' :
        result = a + b

    elif operator == '-' :
        result = a - b

    elif operator == 'x' :
        result = a * b

    elif operator == '/' :
        if b != 0 :
            result = a / b
        else :
            result = "Zero Division Error ! Enter another number b " 

    elif operator == '//' :
        if b != 0 :
            result = a // b
        else :
            result = "Zero Division Error ! Enter another number b "
    elif operator == '%' :
        if b != 0 : 
            result = a % b
        else :
            result = "Zero Division Error ! Enter another number b " 

    return result


# 2 - Define a scientific calculator due to the library numpy :
def science_calculator(a, operator) :
    #Here I want to use another method : dictionnary, I will stock my operators in the dictionnary and then call them later
    #The operator will be the key and the operation its value
    operators = {
        #the trigonometrical functions
        'cos' : lambda: np.cos(a), 
        'sin' : lambda: np.sin(a),
        'tan' : lambda: np.tan(a),
        #the trigonometrical inverse functions
        'arccos' : lambda: np.arccos(a), 
        'arcsin' : lambda: np.arcsin(a),
        'arctan' : lambda: np.arctan(a),
        #the hyperbolic functions
        'cosh' : lambda: np.cosh(a),
        'sinh' : lambda: np.sinh(a),
        'tanh' : lambda: np.tanh(a),
        #the hyperbolic inverse functions
        'arccosh' : lambda: np.arccosh(a),
        'arcsinh' : lambda: np.arcsinh(a),
        'arctanh' : lambda: np.arctanh(a),
        #other functions
        'log' : lambda: np.log10(a) if a >= 0 else 'Error: Negative value',
        'ln' : lambda: np.log(a) if a >= 0 else 'Error: Negative value',
        'exp' : lambda: np.exp(a),
        'abs' : lambda: np.abs(a),
        'root' : lambda: np.sqrt(a) if a >= 0 else 'Error: Negative value below the root',
    }
    #If we create the dictionnary in this way : dict ={'cos' : np.cos(a)}, that means that this operation is done before we call it in the input bloc
    #The solution is to make these functions (operators) as a lambda function or like a reference, then at the end we put it like an arguments in operators.get()
    result = operators.get(operator, lambda:  "Unfound operation")()  #execute the lambda function
    return result #it return a numerical variable, that I can use in the condition down (to round the result if necessary)
     #the programm recuperate the key : operator from the dictionnary operators, if the operator doen't exist, the function return : Unfound operation

################################################################################################################################
#Ask the user the enter the values 
try :
    try :
        try :
        #Ask the user to choose between two types of operators :
            print(f"\n--- Welcome to our calculators !---\n")
            print(f"Please Choose B for basic calculators and S for scientific one")
            choice1 = input(f"Do you want to active 'B' or 'S' ? ").strip().upper()

            if choice1 == 'B' :
                operate = input(f"Enter the operation symbol '+'  '-'  'x'  '/'  '//'  '%' : ").strip()
                number1 = float(input(f"Enter a first number a : "))
                number2 = float(input(f"Enter a second number b : "))
                result1 = basic_calculator(number1, number2, operate)
                print(f"The result of the operation : {number1} {operate} {number2} = {result1}")
                
            elif choice1 == 'S' :
                print(f"Please choose Trigo to operate with trigonometrical function else choose other")
                choice2 = input(f"Do you want to operate with 'Trigo' or 'other' ? ").strip().lower()

                if choice2 == 'trigo' :
                    print(f"Choose 'TF' if you want to operate with trigonometrical functions")
                    print(f"Choose 'TIF' if you want to operate with trigonometrical inverse functions")
                    choice3 = input(f" Do you want 'TF' or 'TIF' ? ").strip().upper()

                    if choice3 == 'TF' :
                        operate = input(f"Enter the operation symbol 'cos'  'sin'  'tan'   'cosh'  'sinh'  'tanh' : ").strip()
                        number = float(input(f"Enter a number of your choice n : "))
                        result2 = science_calculator(np.radians(number), operate)
                        if np.abs(result2) < 1e-10 :
                            result2 = 0.0  #because in python for example cos(pi/2) != 0 exactly
                        print(f"The result of the operation : {operate}({number}) = {result2}")

                    elif choice3 == 'TIF' :
                        operate = input(f"Enter the operation symbol 'arccos'  'arcsin'  'arctan'  'arccosh' 'arcsinh'  'arctanh' : ").strip()
                        number = float(input(f"Enter a number of your choice n : "))
                        result3 = science_calculator(number, operate)
                        print(f"The result of the operation : {operate}({number}) = {result3}")

                elif choice2 == 'other' :
                    operate = input(f"Enter the operation symbol 'log'  'ln'  'exp'  'abs'  'root' : ").strip()
                    number = float(input(f"Enter a number of your choice n : "))
                    result4 = science_calculator(number, operate)
                    print(f"The result of the operation : {operate}({number}) = {result4}")

                else :
                    print(f"Invalide choice. Please enter 'trigonometrical' or 'other")

            else :
                print(f"Invalide choice. Please enter 'basic' or 'scientific")

        except ZeroDivisionError :
            print(f"Erreur : division par zéro")

    except ValueError :
        print("Invalid input. Please enter valid numbers.")

except KeyboardInterrupt :
    print(f"\nExiting ......")