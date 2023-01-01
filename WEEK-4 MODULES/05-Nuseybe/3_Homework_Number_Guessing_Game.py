#Number Guessing Game
# As a player, I want to play a game which I can guess a number the computer chooses in the range I chose.
#  So that I can try to find the correct number which was selected by computer.
# Acceptance Criteria:
# Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer. 
# Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low.
#  If the user guesses correctly, the program should print total time and total number of guesses. 
# You must import some required modules or packages You can assume that the user will enter valid input. (use import random and time)
#written by Nuseybe at 29.12.2022


import random
import math
import time

lower = int(input("Enter Lower bound:- ")) 								# taking lower input
upper = int(input("Enter Upper bound:- "))								# taking upper input 
print(f"You must guess the number between {lower} and {upper}")			
start = time.time()														# time is starting
x = random.randint(lower, upper)										# a nummber is randomly selecting by computer
count = 0

while True:							
	count += 1

	
	guess = int(input("Guess a number:- "))								# taking guessing number as input

	
	if x == guess:														# Condition testing
		print("Congratulations you did it in ",
			count, " try")
		break															# Once guessed, loop will break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You guessed too high!")
end = time.time()														#time is stopping 
time_elapsed = end - start												#calculating the time 

print(time_elapsed)
