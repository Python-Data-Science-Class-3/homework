'''
Author: Adem DOĞAN

Subject of the Program : Number Guessing Game As a player, I want to play a game which 
I can guess a number the computer chooses in the range I chose. So that I can try to find
the correct number which was selected by computer.

Date :12/2022
'''

import random
import time

print("Welcome to the guessing number game")
#It is desired to determine in which number ranges the game should be.
l_limit = int(input("Please Enter Lower Limit!!"))
u_limit = int(input("Please Enter Upper Limit"))

#In these intervals, a number is selected by the computer.
number =random.randint(l_limit, u_limit)

start = time.time()

number_guess = 0
#The game starts and the first choice is requested. The program cycle continues.

while True:
    select_guess= int(input("Enter your guessed number"))

    number_guess += 1

    if (select_guess > number):
        print("Increase estimate \U0001f633 \U0001F44E")
        
    elif(select_guess < number):
        print("Decrease estimate \U0001f633 \U0001f44d ")
        
    else: 
        print("Congrats Guess Right \U0001f973 \U0001f44f") 
        break  

done= time.time()
#Subtracting start time from end time
total_time = done - start
print(f"You guessed the correct number in {number_guess} guesses and {total_time:.2f} seconds!")