""" 

Developer : Melih Orhan Yilmaz
Date      : 28.12.2022

Application : Number Guessing Game

Explanation : 
    As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. So that I can try to find the 
    correct number which was selected by computer.

    Acceptance Criteria:
    Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer. Your program should 
    prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low. If the user guesses 
    correctly, the program should print total time and total number of guesses. You must import some required modules or packages You can assume 
    that the user will enter valid input. (use import random and time)

"""

import random
import time

a = int(input("Please determines the lower limit of the range: "))
b = int(input("Please determines the upper limit of the range: "))

number_guess = 0
random_number = random.randrange(a,b)
guess = int(input("Enter any number: "))
start = time.time() 

while random_number!=guess:
    number_guess += 1
    if guess<random_number:
        print("Your number is less than the random number")
        guess = int(input("Enter number again: "))
    elif guess>random_number:
        print("Your number is greater than the random number")
        guess = int(input("Enter number again: "))
    else:
        break

end = time.time()
duration = end-start

print(f"You guessed the correct number in {number_guess} tries and {duration} seconds.")

