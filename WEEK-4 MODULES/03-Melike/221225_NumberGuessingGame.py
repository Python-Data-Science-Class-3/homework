"""
3- Number Guessing Game 
As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. 
So that I can try to find the correct number which was selected by computer.

Acceptance Criteria: Computer must randomly pick an integer from user selected a range, i.e., from A to B, 
where A and B belong to Integer. Your program should prompt the user for guesses if the user guesses incorrectly, 
it should print whether the guess is too high or too low. If the user guesses correctly, 
the program should print total time and total number of guesses. You must import some required modules or packages 
You can assume that the user will enter valid input. (use import random and time)"""

import random
import time

while True:
    range_start = int(input("\nPlease input the beginning of the range you want to play in: "))
    range_stop = int(input("Please input the end of the range: "))
    total_guess = 1

    while True:
        try:
            start = time.time()
            num_by_comp = random.randint(range_start, range_stop)
            my_guess = int(input("\nYour guess?: "))
            if my_guess == num_by_comp:
                stop = time.time()
                total_time = round(stop-start,2)
                print(f"YOU WON!! The number chosen was {num_by_comp}.\nTotal time of guesses: {total_time} seconds, total number of guesses: {total_guess}")
                break
            elif my_guess > num_by_comp: 
                total_guess +=1
                print("It's too high.. Try again..")
            elif my_guess < num_by_comp: 
                total_guess +=1
                print("It's too low.. Try again..")
        except (TypeError, ValueError) :
            print("Error occured.. Change the values you entered..")


    
### When an incorrect value is entered, it exits the loop and starts over.
### Let's fix it so that it stays in the loop and continues from where it left off.
### Tip: You can use try-except block in the second while loop, then the problem will be cleared.