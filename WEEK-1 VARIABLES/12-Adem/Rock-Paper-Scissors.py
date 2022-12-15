print ("""Welcome to the rock, paper, scissors game.
 Press the letter "R" for Rock, "P" for Paper, "S" for Scissors.
 The game is over when one of the players scores 10. """)
player1 = str(input ("Player1 can enter the name."))
player2 = str(input ("Player2 can enter the name."))
player1_score = 0
player2_score = 0
while (player1_score + player2_score) < 10:
    choice1 = str(input (f"Choice time for {player1} Rock?(R), Paper?(P), Scissors?(S) ")).upper()
    choice2 = str(input (f"Choice time for {player2} Rock?(R), Paper?(P), Scissors?(S)")).upper()
    if choice1 == "R":
        if choice2 == "R":
            print ("You both chose the same things.")
        elif choice2 == "S":
            print (player1," won!!")
            player1_score+=1
        elif choice2 == "P":
            print (player2," won!!")
            player2_score += 1
        else:
            print(player2,"pressed wrong letters ") 
    elif  choice1 == "P":
        if choice2 == "P":
            print ("You both chose the same things.")
        elif choice2 == "R":
            print (player1," won!!")
            player1_score+=1
        elif choice2 == "S":
            print (player2, " won!!")
            player2_score += 1
        else:
            print(player2, " pressed wrong letters ")
    elif  choice1 == "S":
        if choice2 == "S":
            print ("You both chose the same things.")
        elif choice2 == "P":
            print (player1, " won!!")
            player1_score+=1
        elif choice2 == "R":
            print (player2, " won!!")
            player2_score += 1
        else:
            print(player2, "pressed wrong letters ") 
    else:
        print(player1, "pressed wrong letters")

print (f"{player1} score is {player1_score} and {player2} score is {player2_score}")
