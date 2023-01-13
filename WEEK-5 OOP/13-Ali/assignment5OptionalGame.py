'''In this play Scissor Papier Rock user enter player names and enter the number of tour they will play '''

import random
class ScissorPapierRock:
    
    plays = {}
    namen = []
    winner = ""
    PlayRecord = {"rock":"👊", "papier":"✋", "scissors":"✌"}

    def __init__(self, name = ""):
        self.name = name
        ScissorPapierRock.namen.append(self.name)

    @classmethod
    def play2(cls):
        # if len(ScissorPapierRock.namen) == 2:
        for i in ScissorPapierRock.namen:
            ScissorPapierRock.plays[i] = random.choice(["rock","scissors", "papier"])
        # print(ScissorPapierRock.plays)
        if ScissorPapierRock.plays[ScissorPapierRock.namen[0]] != ScissorPapierRock.plays[ScissorPapierRock.namen[1]]:
            print(f"{ScissorPapierRock.namen[0]} spielt {ScissorPapierRock.PlayRecord[ScissorPapierRock.plays[ScissorPapierRock.namen[0]]]}")
            print(f"{ScissorPapierRock.namen[1]} spielt {ScissorPapierRock.PlayRecord[ScissorPapierRock.plays[ScissorPapierRock.namen[1]]]}")
        ScissorPapierRock.comparing()

    @classmethod
    def comparing(cls):
        # if len(ScissorPapierRock.plays) == 2:
        if ScissorPapierRock.plays[ScissorPapierRock.namen[0]] != ScissorPapierRock.plays[ScissorPapierRock.namen[1]]:
            if ScissorPapierRock.plays[ScissorPapierRock.namen[0]] == "papier" and ScissorPapierRock.plays[ScissorPapierRock.namen[1]] == "rock":
                ScissorPapierRock.winner = ScissorPapierRock.namen[0]
            elif ScissorPapierRock.plays[ScissorPapierRock.namen[1]] == "papier" and ScissorPapierRock.plays[ScissorPapierRock.namen[0]] == "rock":
                ScissorPapierRock.winner = ScissorPapierRock.namen[1]
            elif ScissorPapierRock.plays[ScissorPapierRock.namen[0]] == "papier" and ScissorPapierRock.plays[ScissorPapierRock.namen[1]] == "scissors":
                ScissorPapierRock.winner = ScissorPapierRock.namen[1]
            elif ScissorPapierRock.plays[ScissorPapierRock.namen[1]] == "papier" and ScissorPapierRock.plays[ScissorPapierRock.namen[0]] == "scissors":
                ScissorPapierRock.winner = ScissorPapierRock.namen[0]
            elif ScissorPapierRock.plays[ScissorPapierRock.namen[0]] == "rock" and ScissorPapierRock.plays[ScissorPapierRock.namen[1]] == "scissors":
                ScissorPapierRock.winner = ScissorPapierRock.namen[0]
            elif ScissorPapierRock.plays[ScissorPapierRock.namen[1]] == "rock" and ScissorPapierRock.plays[ScissorPapierRock.namen[0]] == "scissors":
                ScissorPapierRock.winner = ScissorPapierRock.namen[1]
            print("the winner of the round is {}".format(ScissorPapierRock.winner))
        else:
            ScissorPapierRock.play2()
        
        
player1 = ScissorPapierRock(input("enter please name1 :"))       
player2 = ScissorPapierRock(input("enter please name2 :"))          

n = int(input("enter the number you want it plays: "))     
        

while n > 0 :
    ScissorPapierRock.play2() 
    n -= 1
        
            

            

