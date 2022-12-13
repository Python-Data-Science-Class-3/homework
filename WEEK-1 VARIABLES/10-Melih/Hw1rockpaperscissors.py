""" 
Developer : Melih Orhan Yilmaz
Date      : 05.12.2022

Application : Rock-Paper-Scissors

Explanation : Take the names of the players and play the stone - paper - scissors game. Game 10 hands it will last. 
At the end of 10 hands, the winner will be determined. The score will be displayed at the end.

 """

name1 = input('Enter your name user1: ')
name2 = input('Enter your name user2: ')
name1point = 0
name2point = 0
totalGamePoint = 10

while (name1point + name2point != totalGamePoint) :
    name1choice = int(input(f"What's your choice {name1}? \n1. Rock\n2. Paper\n3. Scissors\n"))
    name2choice = int(input(f"What's your choice {name2}? \n1. Rock\n2. Paper\n3. Scissors\n"))

    if name1choice == name2choice :
        print("Draw")
    elif (name1choice == 1 and name2choice == 3) | (name1choice == 2 and name2choice == 1) | (name1choice == 3 and name2choice == 2) :
        print(f"{name1} won.")
        name1point += 1
    else :
        print(f"{name2} won.")
        name2point += 1

print (f"{name1} score: {name1point}\n{name2} score: {name2point}")       

if name1point == name2point :
        print("Draw".upper())
elif name1point >= name2point :
        print(f"{name1} won the game.".upper())
else :
        print(f"{name2} won the game.".upper())