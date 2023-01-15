
gamer_1 = input("Please input first player: ")
gamer_2 = input("Please input second player: ")

#to add score to the gamer scores each round, those scores are fistly assigned to zero.
score_1 = 0
score_2 = 0

print ("To begin the game please choose rock (R), Scissors (S) or paper (P)...")

#till 10 rounds is played, it will contunie to ask: while loop.
while True:
    for i in range(1,11):
        print(f"{i}. round:")
        #to remove upper lower case sensitivity in inputs:
        chose_1 = input(f"{gamer_1}: ").upper()
        chose_2 = input(f"{gamer_2}: ").upper()
        #to determine which move beats:
        if (chose_1 == "R" and chose_2 == "P") or (chose_1 == "P" and chose_2 == "S") or (chose_1 == "S" and chose_2 == "R"):
            score_2 += 1
        elif (chose_1 == "R" and chose_2 == "S") or (chose_1 == "P" and chose_2 == "R") or (chose_1 == "S" and chose_2 == "P"):
            score_1 += 1
        elif (chose_1 == "R" and chose_2 == "R") or (chose_1 == "P" and chose_2 == "P") or (chose_1 == "S" and chose_2 == "S") :
            continue
        else:
            print("Invalid input..")
        #score results:
        print(f"{gamer_1} : {score_1}       {gamer_2} : {score_2} ")
    
    while i == 10:
        if (score_1 > score_2):
            print(f"Game over.. {gamer_1} won!!")
        elif (score_1 < score_2):
            print(f"Game over.. {gamer_2} won!!")
        else:
            print("It's a tie..")
        quit()