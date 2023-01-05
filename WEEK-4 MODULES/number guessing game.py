#As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. 
#So that I can try to find the correct number which was selected by computer.

#Acceptance Criteria:
#Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer. 
#Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low. 
#If the user guesses correctly, the program should print total time and total number of guesses. 
#You must import some required modules or packages You can assume that the user will enter valid input. (use import random and time)


from random import randint
import time
start=time.time()

print("***Welcome To Number Guessing Game***")

x=int(input("Range First: "))
y=int(input("Range Last: "))

rand=randint(x,y) #number range to choose
count=0  #the counter that will increase with each wrong guess
while True:
    count+=1
    number=int(input("Please enter a number:"))
    if (number<rand):
       print("Your guess is too low.")
       continue
    elif (number>rand):
       print("Your guess is too high.") 
       continue
    else:
        print("Randomly chosen number{0}:".format(rand))
        print("Your guess count: {0}".format(count))

    finish=time.time()
    print("Your total game time:",finish-start)

 