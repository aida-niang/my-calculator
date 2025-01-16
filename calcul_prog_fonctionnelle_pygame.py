#In this version, I will define only one function in which I will use numpy operators for addition, multiplication .....
#import the necessary libraries :
import numpy as np
import matplotlib.pyplot as plt

#######################################################################

#define the functions :
# - Define a scientific calculator due to the library numpy :
def science_calculator(a, b, operator) :
    #Here I want to use another method : dictionnary, I will stock my operators in the dictionnary and then call them later
    #The operator will be the key and the operation its value
    #Her I call the library numpy which is in reality a calculator
    operators = {
        #basic operators
        '+' : lambda: a + b,
        '-' : lambda: a - b,
        'x' : lambda: a * b,
        '/' : lambda: a / b if b != 0 else "Zero Division Error ! Enter another number b",
        '//' : lambda: a // b if b != 0 else "Zero Division Error ! Enter another number b",
        '%' : lambda: a % b if b != 0 else "Zero Division Error ! Enter another number b",
        #the trigonometrical functions
        'cos' : lambda: np.cos(a), 
        'sin' : lambda: np.sin(a),
        'tan' : lambda: np.tan(a),
        #the trigonometrical inverse functions
        'arccos' : lambda: np.arccos(a) if -1 <= a <= 1 else "Input out of range [-1, 1]",
        'arcsin' : lambda: np.arcsin(a) if -1 <= a <= 1 else "Input out of range [-1, 1]",
        'arctan' : lambda: np.arctan(a),
        #the hyperbolic functions
        'cosh' : lambda: np.cosh(a),
        'sinh' : lambda: np.sinh(a),
        'tanh' : lambda: np.tanh(a),
        #the hyperbolic inverse functions
        'arccosh' : lambda: np.arccosh(a) if a >= 1 else "Input must be >= 1",
        'arcsinh' : lambda: np.arcsinh(a),
        'arctanh' : lambda: np.arctanh(a) if -1 < a < 1 else "Input out of range (-1, 1)",
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

###########################################################################################################""

#Ask the user the enter the values
try :
    try :
        try :
       
            print(f"\n--------------------------- Welcome to our calculator !-------------------------------\n")
            print(f"\n1 - Choose B to use basic operators")
            print(f"2 - Choose Trigo to operate with trigonometrical")
            print(f"3 - Choose other for other scientific operations")
            while True : #when the entered value or symbol is not valid, there is a printed message but I want that my programme is executed again to allow the user to enter the values or the symbols again
            #I add while True before each input, in order to ask the user to try again, if the entered value is not valid

                choice2 = input(f"\n- Do you want to operate with 'B' , 'Trigo' or 'other' ? ").strip().lower()

                if choice2 == 'b' :
                    print(f"\nTou are operating with basic operators")
                    operate = input(f"- Enter the operation symbol '+'  '-'  'x'  '/'  '//'  '%'   : ").strip()
                    if operate not in ['+'  '-'  'x'  '/'  '//'  '%'] :
                        print 
                    number1 = float(input(f"- Enter a first number a : "))
                    number2 = float(input(f"- Enter a second number b : "))
                    result1 = science_calculator(number1, number2, operate)
                    print(f"The result of the operation : {number1} {operate} {number2} = {result1}")



                elif choice2 == 'trigo' : 
                    print(f"\nTou are operating with trigonometrical functions")
                    print(f"\n5 - Choose 'TF' if you want to operate with trigonometrical functions")
                    print(f"6 - Choose 'TIF' if you want to operate with trigonometrical inverse functions")
                    choice3 = input(f" Do you want 'TF' or 'TIF' ? ").strip().upper()

                    if choice3 == 'TF' :
                        operate = input(f"\n- Enter the operation symbol 'cos'  'sin'  'tan'   'cosh'  'sinh'  'tanh' : ").strip()
                        number = float(input(f"- Enter a number of your choice n : "))
                        result2 = science_calculator(np.radians(number), operate)
                        if np.abs(result2) < 1e-10 :
                            result2 = 0.0  #because in python for example cos(pi/2) != 0 exactly
                        print(f"The result of the operation : {operate}({number}) = {result2}")

                    elif choice3 == 'TIF' :
                        operate = input(f"\n- Enter the operation symbol 'arccos'  'arcsin'  'arctan'  'arccosh' 'arcsinh'  'arctanh' : ").strip()
                        number = float(input(f"- Enter a number of your choice n : "))
                        result3 = science_calculator(number, operate)
                        print(f"The result of the operation : {operate}({number}) = {np.radians(result3)}")

                    else :
                        print(f"\n --!-- Invalide choice. Please enter 'TF' or 'TIF' ")

                                    

                elif choice2 == 'other' :
                    operate = input(f"\n- Enter the operation symbol 'log'  'ln'  'exp'  'abs'  'root' : ").strip()
                    number = float(input(f"- Enter a number of your choice n : "))
                    result4 = science_calculator(number, operate)
                    print(f"The result of the operation : {operate}({number}) = {result4}")

                else :
                    print(f" --!-- Invalide choice. Please enter 'B' , 'trigo' or 'other' ")
   

                retry = input(f"Do you want to run again this calculator (Yes / No)? ").strip().lower()
                if retry != 'yes' :
                    print(f"Thank you. Good Bye !")
                    exit()

        except ZeroDivisionError :
                print(f"Erreur : division par zéro")

    except ValueError :
            print("Invalid input. Please enter valid numbers.")

except KeyboardInterrupt :
        print(f"\nExiting ......")
        