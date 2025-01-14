#import the necessary libraries :
import numpy as np
import matplotlib.pyplot as plt

########################################################################
#define the functions :
# 1 - Define a basic calculator with basic operators : +, x,
def calculator(a, b, operator) :
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

    return "The result of the operation : a {operator} b = {result}"


# 2 - Define a scientific calculator due to the library numpy :
def science_calculator(a, b, opertor_s) :
    #Here I want to use another method : dictionnary, I will stock my operators in the dictionnary and then call them later
    #The operator will be the key and the operation its value
    opertor_s = {
        'cos' : np.cos(a),
        'sin' : np.sin(a),
        'tan' : np.tan(a)
        'sinh' : np.sin(a)
    }

#Ask the use the enter the values and the operator :
try :
    number1 = int(input(f"Enter a first number a : "))
    number2 = int(input(f"Enter a second number b : "))
    operate = input(f"Enter the operation symbol '+'  '-'  'x'  '/'  '//'  '%' : ")

    calculator(number1, number2, operate)

except ZeroDivisionError :
    print(f"Erreur : division par zéro")
