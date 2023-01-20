'''
Developer   : Musab SARI
Date        : 01.01.2023

Application : Number Guessing Game

Explanation : Number Guessing Game is an application where user can play a fun game with computer. Computer randomly picks a number 
between the range which is defined by the user and user tries to find it with guess inputs.
'''

import random
import time

value = random.randint(int(input('Lower limit:')),int(input('Upper limit:')))
count = 0

starttime = time.time()

while True:
    
    user_guess = int(input('Guess:'))
    count += 1

    if value == user_guess:

        stoptime = time.time()

        print(f'Congratulations! You found it.\nNumber of guesses: {count}','Time spent: %3.2f' %(stoptime - starttime), 'seconds')

    elif value > user_guess:

        print('Incorrect! Your guess is too low! Try again')
    
    elif value < user_guess:

        print('Incorrect! Your guess is too high! Try again')