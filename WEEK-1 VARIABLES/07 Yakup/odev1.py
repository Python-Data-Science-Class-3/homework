import random   #library was imported.
print('''      
                  ROCK PAPER SCISSORS
1. The stone cuts the scissors and the stone wins in this drum.
2. The paper wraps around the stone and wins the paper in this drum.
3. Scissors cuts the paper, and in this case, scissors win.
''' )
my_list= ['stone', 'paper','scissors']
player_1 = input('1. player\'s first and last name').upper()
player_2 = input('2. player\'s first and last name').upper()
count_1 = 0
count_2 = 0 
for i in range(1,11):

    player_1_hand = random.choice(my_list)     #The game will continue 10 times,
                                                # but the 1st player will get a random hand from the list. 
                                                #But the other player will be asked to write his own hand.
    player_2_hand = input('write your choice on the screen = ').lower() 

    if player_1_hand == 'stone' and player_2_hand == 'scissors' :
        print (f' {i}. hand winner {player_1} and and your score {count_1 + 5} ')
        count_1 += 5
    elif player_1_hand == 'stone' and player_2_hand == 'paper' :
         print (f' {i}. hand winner {player_2} and and your score {count_2+5} ')
         count_2 += 5
    elif player_1_hand == player_2_hand :
        print (f" {i}.  the hand is tied your points drum {count_1} and {count_2}  ")
    elif player_1_hand == 'peper' and player_2_hand == 'stone' :
         print (f' {i}. hand winner {player_1 } and and your score {count_1+5} ')
         count_1 += 5
    elif player_1_hand == 'peper' and player_2_hand== 'scissors' :
         print (f' {i}. hand winner {player_2} and and your score{count_2+5}   ')
         count_2 += 5
    elif player_1_hand== 'scissors' and player_2_hand == 'stone' :
        print (f' {i}. hand winner {player_2} and and your score {count_2+5}  . ')
        count_2 += 5
    elif player_1_hand == 'scissors' and player_2_hand == 'peper' :
         print (f' {i}. hand winner {player_1} and and your score {count_1+5} . ')
         count_1 += 5
         
    
if count_1 > count_2 :
    print("\n")
    print(f" winner {player_1} your score  {count_1}   the loser {player_2} your score {count_2}  ")
elif count_1 < count_2 :
    print("\n")
    print(f" winner {player_2} your score{count_2}  the loser {player_1} your score {count_1}  ")
else :
    print("\n")
    print(f"The game is over in a draw....your score 1. player {count_1} 2. player{count_2}  ")
    print("ln")










