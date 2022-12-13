'''
Developer   : Musab SARI
Date        : 06.12.2022

Application : Rock-Paper-Scissors Game

Explanation : Rock-Paper-Scissors is a well-known ageless and very old game. Two players play it to decide winner of a case or to solve a conflict.
In this game, stone has an advantage over scissors, scissors have an advantage over paper and paper has an advantage over stone, 
which puts the situation in a paradox in terms of superiority.
'''
Player1 = input("Name player 1:") # user input for platyer 1 name
Player2 = input("Name player 2:") # user input for player 2 name
count = score1 = score2 = 0

while count < 10:
    print(f"{10 * '_'}\nRound {count + 1}!\n{10 * '~'}\nRock, Paper or Scissors? Pick one!\nNote: Game is not case sensitive!\nRock=R/r, Paper=P/p, Scissors=S/s")#Introduction of the game
    Choise_player_1 = input(f"{Player1} Choose one: R, P or S?\nChoice:") # user input for player 1 choice
    Choise_player_2 = input(f"{Player2} Choose one: R, P or S?\nChoice:") # user input for player 2 choice
    
    if Choise_player_1 and Choise_player_2 in ['r','p','s']:#to make the game non case sensitive
        Choise_player_1 = Choise_player_1.upper()
        Choise_player_2 = Choise_player_2.upper()
    # below is the functions that create game mechanics
    if (Choise_player_1 == "R") and (Choise_player_2 == "R") or (Choise_player_1 == "P") and (Choise_player_2 == "P") or (Choise_player_1 == "S") and (Choise_player_2 == "S"): 
        print("It is a tie!")
        print("No points for each side")
    
    elif (Choise_player_1 == "R") and (Choise_player_2 == "P") or (Choise_player_1 == "P") and (Choise_player_2 == "S") or (Choise_player_1 == "S") and (Choise_player_2 == "R"):
        print(f"{Player2} wins {(count+1)}. round!")
        score2 += 1
    
    elif (Choise_player_1 == "R") and (Choise_player_2 == "S") or (Choise_player_1 == "P") and (Choise_player_2 == "R") or (Choise_player_1 == "S") and (Choise_player_2 == "P"):
        print(f"{Player1} wins {(count+1)}. round!")
        score1 += 1
    
    else:
        print("Wrong Entry! Please try again!")
        continue
    count += 1

print(18*'~') # to make user friendly interface

print(f'Score of {Player1} is {score1}\nScore of {Player2} is {score2}')

if score1 > score2: # output for exhibition of the winner
    print(f"{Player1} wins the game!")

elif score2 > score1:
    print(f"{Player2} wins the game!")

else:
    print("It is a tie!")