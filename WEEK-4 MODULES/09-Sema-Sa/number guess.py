
import time
import random
import datetime
x = int(input("Enter lower number:"))
y = int(input("Enter upper number:"))
number = random.randint(x,y)
guess = 0
print(" Start  timer :")
a = datetime.datetime.now()
while True :
    user_guess = int(input("Please guess the number ,lets go:"))
    if user_guess>number:
        print("your guess is higher than the number")
        guess +=1
    elif user_guess<number:
        print("your guess is lower than the number")
        guess +=1
    else :
        b = datetime.datetime.now()
        howmanytime = b - a
        print("Congratulations")
        guess +=1
        print(guess," times guessed")
        print(howmanytime.seconds, "seconds")
        break