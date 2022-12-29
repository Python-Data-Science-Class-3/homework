'''4- Mis Calculator
As a user, I want to use a program which can calculate basic mathematical
operations. So that I can add, subtract, multiply or divide my inputs.
Acceptance Criteria:
The calculator must support the Addition, Subtraction, Multiplication 
and Division operations. Define four functions in four files for each 
of them, with two float numbers as parameters. To calculate the answer,
use math.ceil() and get the next integer value greater than the result 
Create a menu using the print command with the respective options and 
take an input choice from the user. Using if/elif statements for cases 
and call the appropriate functions. Use try/except blocks to verify 
input entries and warn the user for incorrect inputs. Ask user if 
calculate numbers again. To implement this, take the input from user Y 
or N. (use import sys, ceil function in math)'''   
from math import ceil
from assignmetMultiplication import* # 4 moduls have 4 math options
from assignmentAddition import*
from assignmentDivision import*
from assignmentSubtraction import* 
import sys
while True:
    try:
        operandA = float(input("please enter first operand: "))
        operandB = float(input("please enter second operand: "))
        break
    except ValueError:
        print("enter please only float❗")    
while True:  
    try:
        operation = input("enter one of the mathematical operations \"+\" , \"-\", \"*\" or \"/\" : ")
        assert (operation == "+"or  #in this step enter user a operation 
                operation == "-"or  # and if user not enter one of them 
                operation == "*"or  # pops a warnung
                operation == "/")
        break
    except AssertionError:
        print("enter please an valid operation")        

def operate(operand1, operand2):   # in this step operate via uther modules
    if operation == "*":
        return multiple(operand1, operand2)
    elif operation == "-":
        return subtract(operand1, operand2) 
    elif operation == "/":
        return devide(operand1, operand2)
    elif operation == "+":
        return add(operand1, operand2)

        
outcome = operate(operandA, operandB)
consequence = ceil(outcome) 
print(consequence)



