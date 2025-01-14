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

    return f"The result of the operation : a {operator} b = {result}"


# 2 - Define a scientific calculator due to the library numpy :
def science_calculator(a, operator) :
    #Here I want to use another method : dictionnary, I will stock my operators in the dictionnary and then call them later
    #The operator will be the key and the operation its value
    operators = {
        #the trigonometrical functions
        'cos' : np.cos(a), 
        'sin' : np.sin(a),
        'tan' : np.tan(a),
        #the trigonometrical inverse functions
        'arccos' : np.arccos(a), 
        'arcsin' : np.arcsin(a),
        'arctan' : np.arctan(a),
        #the hyperbolic functions
        'cosh' : np.cosh(a),
        'sinh' : np.sinh(a),
        'tanh' : np.tanh(a),
        #the hyperbolic inverse functions
        'arccosh' : np.arccosh(a),
        'arcsinh' : np.arcsinh(a),
        'arctanh' : np.arctanh(a),
        #other functions
        'log' : np.log10(a) if a >= 0 else 'Error: Negative value',
        'ln' : np.log(a) if a >= 0 else 'Error: Negative value',
        'exp' : np.exp(a),
        'abs' : np.abs(a),
        'root' : np.sqrt(a) if a >= 0 else 'Error: Negative value below the root',
    }

    return f"The result of this operation is :{operators.get(operator, "opérateur invalide")}"


#Ask the use the enter the values 
try :
#Ask the user to choose between two types of operators :
    print(f"Welcome to our calculator ! \n")
    choice1 = input(f"Choose the calculator type (basic / scientific) :").strip().lower()

    if choice1 == 'basic' :
        operate = input(f"Enter the operation symbol '+'  '-'  'x'  '/'  '//'  '%' : ")
        number1 = int(input(f"Enter a first number a : "))
        number2 = int(input(f"Enter a second number b : "))
        basic_calculator(number1, number2, operate)
        
    elif choice1 == 'scientific' :
        choice2 = input(f"Choose the operator type (trigonometrical / other) :").strip().lower()
        if choice2 == 'trigonometrical' :
            operate = input(f"Enter the operation symbol 'cos'  'sin'  'tan'  'arccos'  'arcsin'  'arctan'  'cosh'  'sinh'  'tanh'  'arccosh' 'arcsinh'  'arctanh' : ")
            number = int(input(f"Enter a number of your choice n : "))
            science_calculator(number, operate)

        elif choice2 == 'other' :
            operate = input(f"Enter the operation symbol 'log'  'ln'  'exp'  'abs'  'root' : ")  
            number = int(input(f"Enter a number of your choice n : "))
            science_calculator(number, operate)

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


  