import random

user1 = input("1.player\n")
user2 = input("2.player\n")
options = ['rock', 'paper', 'scissor']
user1_win = 0
user2_win = 0

for i in range(1,11) :

    user1_hand = options[random.randint(0,2)]
    user2_hand = options[random.randint(0,2)]
    print(f"{user1} = {user1_hand} \n{user2} = {user2_hand}")

    if user1_hand == user2_hand : 
        print(f"{i}.tur draw")
    elif user1_hand == 'rock' and user2_hand == 'paper' :
        print(f"{i}.tur {user2} won. ")
        user2_win += 1
    elif user1_hand == 'rock' and user2_hand == 'scissor' :
        print(f"{i}.tur {user1} won.")
        user1_win += 1
    elif user1_hand == 'paper' and user2_hand == 'rock' :
        print(f"{i}.tur {user1} won.")
        user1_win += 1
    elif user1_hand == 'paper' and user2_hand == 'scissor' :
        print(f"{i}.tur {user2} won.")
        user2_win += 1
    elif user1_hand == 'scissor' and user2_hand == 'rock' :
        print(f"{i}.tur {user2} won.")
        user2_win += 1
    elif user1_hand == 'scissor' and user2_hand == 'paper' :
        print(f"{i}.tur {user1} won.")
        user1_win += 1
    print(f"{user1} scored = {user1_win} \n{user2} scored= {user2_win}")
    next_tour = input("enter for the next tour...\n")


if user1_win > user2_win:
    print(f"{user1} won. Congruation...")
elif user1_win < user2_win :
    print(f"{user2} won. Congruation...")
else :
    print("its draw , Brotherhood won..")