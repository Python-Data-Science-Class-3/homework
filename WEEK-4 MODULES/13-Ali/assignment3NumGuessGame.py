'''3- Number Guessing Game
As a player, I want to play a game which I can guess a number the computer
chooses in the range I chose. So that I can try to find the correct number 
which was selected by computer.
Acceptance Criteria:
Computer must randomly pick an integer from user selected a range, i.e., from
A to B, where A and B belong to Integer. Your program should prompt the user 
for guesses if the user guesses incorrectly, it should print whether the 
guess is too high or too low. If the user guesses correctly, the program 
should print total time and total number of guesses. You must import some 
required modules or packages You can assume that the user will enter valid 
input. (use import random and time)
https://pynative.com/python-get-time-difference/#:~:text=To%20get%20the%20difference%20between%20two%2Dtime%2C%20subtract%20time1%20from,time%20to%20the%20microsecond%20resolution.&text=To%20get%20a%20time%20difference%20in%20seconds%2C%20use%20the%20timedelta.
'''
import random
from datetime import datetime
lowerBound = input("choose two numbers boundary of range: from: ")
upperBound = input("to: ")

secretNumber = random.randrange(int(lowerBound), int(upperBound)+1)
# print(secretNumber)

start_time = datetime.utcnow()
# print(start_time)

guessNumber = int()
while secretNumber != guessNumber:
    guessNumber = int(input("enter your guess: "))
    print("wrong answer❗ ❌ try please again")
    if (guessNumber < secretNumber and
        secretNumber - guessNumber > 10):
        print("your guess is too low")
    elif (guessNumber < secretNumber and
        secretNumber - guessNumber > 5):
        print("your guess is low")
    elif (guessNumber < secretNumber and
        secretNumber - guessNumber <= 5):
        print("your guess is a bit low")
    elif (guessNumber > secretNumber and
        guessNumber- secretNumber > 10):
        print("your guess is too high")
    elif (guessNumber > secretNumber and
         guessNumber - secretNumber > 5):
        print("your guess is high")
    elif (guessNumber > secretNumber and
        guessNumber - secretNumber <= 5):
        print("your guess is a bit high")
        
if secretNumber == guessNumber:    
    print("correct answer! CONGRATULATIONS 🎉💯")
end_time = datetime.utcnow()  
# print(end_time)  
delta = end_time - start_time
print(f"your playing for correct guess lasted {delta.total_seconds()} seconds")# time difference in seconds