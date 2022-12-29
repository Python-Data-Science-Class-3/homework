'''
Number Guessing Game As a player, I want to play a game which I can guess a number
the computer chooses in the range I chose. So that I can try to find the correct 
number which was selected by computer.

Acceptance Criteria: Computer must randomly pick an integer from user selected a
range, i.e., from A to B, where A and B belong to Integer. Your program should prompt
the user for guesses if the user guesses incorrectly, it should print whether the
guess is too high or too low. If the user guesses correctly, the program should
print total time and total number of guesses. You must import some required modules 
or packages You can assume that the user will enter valid input. 
(use import random and time)


''' 
#--------------------Made by Yunus 27.12.2022-------------
import random as rd
import time

borders = list(map(int,input("Pls enter the range :").split()))
number = rd.randint(borders[0],borders[1])                                        #random number in range
# print(number)
value = True
nmb_of_guesses = 0
start = time.time()                     #stars time
while value:                            #while loop to guessing until correct guess
    guess = int(input("Please enter your guess : \n"))      
    
    nmb_of_guesses +=1                  #counts number of guesses
    if guess == number:                 
        print("Well done captain, you have some skills")
        end = time.time()               #ends time upon true guess
        print("Number of total guesses are : ",nmb_of_guesses)
        print("you have done it in ",round((end - start),2),"seconds")
        value = False                    #ends the while loop
    elif guess+(borders[1]-borders[0])/4 < number:      # the logic is if guess is lower than quarter of total numbers
        print("Thats too low!")
    elif guess-(borders[1]-borders[0])/4 > number:      # the logic is if guess is greater than quarter of total numbers
        print("Thats too high!")
    elif abs(guess-number) < (borders[1]-borders[0])/4: # the logic is if guess is in between quarter of total numbers
        print("That was close")

        

    