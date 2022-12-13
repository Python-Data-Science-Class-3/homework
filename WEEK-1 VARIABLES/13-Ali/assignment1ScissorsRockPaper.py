'''1. Rock-Paper-Scissors
    Take the names of the players and play the stone - paper - 
    scissors game. game 10 hands it will last. At the end of 
    10 hands, the winner will be determined. The score will 
    be displayed at the end.m?isFullScreen=true'''
import random

player1 = input("enter name player1: ")
player2 = input("enter name player2: ")
i = 0
scorePlayer1 = 0
scorePlayer2 = 0
while i < 10:   
    a = {"rock":'''      
        _______
    ---'   ____)
         (_____)
         (_____)
          (____)
    ---.__(___)     
        ''', 
         "paper":'''
        _______
    ---'   ____)____
            ________)
            _________)
            ________)
    ---._________) 
         ''', 
         "scissors":'''
        _______
    ---'   ____)____
            ________)
        _____________)
          (____)
    ---.__(___)     
        '''
         }
    
    player1_play = random.choice(["rock", "paper", "scissors"])
    player2_play = random.choice(["rock", "paper", "scissors"])
    
    if player1_play != player2_play:    
        print("tour", str(i+1) + ":")
        # print('%-40s%-40s' % (f"{player1} played ", f"{player2} played")) 
        
        # print(a[player1_play] + a[player2_play]) 
        
        # print(a[player1_play], end= ' ') 
        # print(a[player2_play]) 
        # print(a[player1_play], a[player2_play], sep= '         ') 
        # print('%-10s%-10s' % (a[player1_play], a[player2_play]))
        
        print('%-10s%-15s%-15s' % ('',f"{player1} played", a[player1_play])) 
        print('%-10s%-15s%-15s' % ('',f"{player2} played", a[player2_play]))  
        # print('%-1s%-15s' % ('',f"{a[player1_play]}",), sep='', end= '')  
        # print('%-40s%-40s' % ('',a[player2_play]))  
        i += 1
    else:
        continue 
    if player1_play == 'rock' and player2_play == 'scissors':
        print('%-30s%-20s' % ('',f' {player1.upper()} wins'))
        scorePlayer1 += 1
    elif player1_play == 'rock' and player2_play == 'paper':
        print('%-30s%-20s' % ('',f' {player2.upper()} wins')) 
        scorePlayer2 += 1   
    elif player1_play == 'scissors' and player2_play == 'paper':
        print('%-30s%-20s' % ('',f' {player1.upper()} wins'))  
        scorePlayer1 += 1     
    elif player1_play == 'scissors' and player2_play == 'rock':
        print('%-30s%-20s' % ('',f' {player2.upper()} wins'))
        scorePlayer2 += 1 
    elif player1_play == 'paper' and player2_play == 'scissors':
        print('%-30s%-20s' % ('',f' {player2.upper()} wins'))   
        scorePlayer2 += 1 
    elif player1_play == 'paper' and player2_play == 'rock':
        print('%-30s%-20s' % ('',f' {player1.upper()} wins'))        
        scorePlayer1 += 1
print(f'{player1.upper()} won {scorePlayer1} time/s')
print(f'{player2.upper()} won {scorePlayer2} time/s')    
if scorePlayer1 < scorePlayer2:
    print(f'end-grade winner {player2} 🎉')
elif scorePlayer1 > scorePlayer2:    
    print(f'end-grade winner {player1} 🎉')
else:
    print(f'{player1} and {player2} are draw')
    
    
    