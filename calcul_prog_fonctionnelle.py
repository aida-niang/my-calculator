#import the necessary libraries :
import numpy as np
import matplotlib.pyplot as plt


#initialize the variables (if you want to work with global variables)

#define the functions :
def calculator(a, b, operator) :
    if operator == '+' :
        result = a + b


    elif operator == '-' :
        result = a - b


    elif operator == '*' :
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

    return print(f"The result of the operation : a {operator} b = {result}")

    ##Add the numpy functions : cos, sin, log, exp n! .....

#Ask the use the enter the values and the operator :
try :
    number1 = int(input(f"Enter a first number a : "))
    number2 = int(input(f"Enter a second number b : "))
    operate = input(f"Enter the operation symbol '+'  '-'  '*'  '/'  '//'  '%' : ")

    calculator(number1, number2, operate)

except ZeroDivisionError :
    print(f"Erreur : division par zéro")
