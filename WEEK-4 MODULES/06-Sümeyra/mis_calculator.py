# As a user, I want to use a program which can calculate basic mathematical operations. 
# So that I can add, subtract, multiply or divide my inputs.

# Acceptance Criteria:
# The calculator must support the Addition, Subtraction, Multiplication and Division operations. D
# efine four functions in four files for each of them, with two float numbers as parameters. 
# To calculate the answer, use math.ceil() and get the next integer value greater than the result 
# Create a menu using the print command with the respective options and take an input choice from the user. 
# Using if/elif statements for cases and call the appropriate functions.
#  Use try/except blocks to verify input entries and warn the user for incorrect inputs. 
# Ask user if calculate numbers again. To implement this, take the input from user Y or N. (use import sys, ceil function in math)

### 'except ValueError:' line does not work. The program stops when an incorrect value is entered. Can we fix it?

import sys
import math as m

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:   
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = float(input('Please enter the first number: '))
    number_2 = float(input('Please enter the second number: '))
    try:
         if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(m.ceil(number_1 + number_2))

         elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(m.ceil(number_1 - number_2))

         elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(m.ceil(number_1 * number_2))

         elif operation == '/':
            print('{} / {} = '.format(number_1, number_2))
            print(m.ceil(number_1 / number_2))

         else:
            print("You have not typed a valid operator, please run the program again.")

    except ValueError:
        print("Please enter a number:")
        
    except ZeroDivisionError:
        print(f"Second number = 0\n{number_1} can't be divided by zero\nPlease enter a different number:")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print("Okay,bye!")
    else:
        again()

calculate()
