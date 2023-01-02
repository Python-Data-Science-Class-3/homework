'''
 As a player, I want to play a game which I can guess a number the computer chooses
 in the range I chose.So that I can try to find the correct number which was selected 
 by computer.

Acceptance Criteria:

Computer must randomly pick an integer from user selected a range, i.e., 
from A to B, where A and B belong to Integer. Your program should prompt 
the user for guesses if the user guesses incorrectly, it should print whether
the guess is too high or too low. If the user guesses correctly,
 the program should print total time and total number of guesses. 
 You must import some required modules or packages You can assume that the user 
 will enter valid input. (use import random and time)
'''


import random
import time
import os


t = time.localtime(time.time()).tm_sec  #   I only used  for secunt.   'tm_min'  for minuut
count =0
nummer = random.choice(range(1,101))


while True :
    gues = int(input("give a nummer : \n"))
    count+=1
    if gues>nummer :
        print("give a lower number please.\n")
    elif gues<nummer:
        print("give a higher number please.\n")

    elif gues==nummer:
        break
os.system('cls')    # for windows : clear the terminal

print(f" Yuppy '{t}' minutes you guessed right... ")       
print("\n")