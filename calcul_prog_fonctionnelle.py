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
            print(f"Enter another number (b) not nul")  


    elif operator == '//' :
        if b != 0 :
            result = a // b
        else :
            print(f"Enter another number (b) not nul")

    elif operator == '%' :
        if b != 0 : 
            result = a % b
        else :
            print(f"Enter another number (b) not nul") 

    ##Add the numpy functions : cos, sin, log, exp n! .....

#Ask the use the enter the values and the operator :
