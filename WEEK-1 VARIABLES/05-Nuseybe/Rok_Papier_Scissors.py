import random
gamechoise=["p","s","r"]
p = gamechoise[0]
s = gamechoise[1]
r = gamechoise[2]
compscore = 0
userscore = 0
i=0
while True : 
    comp = random.choice(gamechoise)
    user= input(" Please input a choise for gaming: for papier 'p', for scissors 's', for rock 'r'")
    if user == p :
        if comp == s :
         userscore += 1
         print(compscore)  
         print(userscore)
        elif comp == s: 
         compscore += 1
         print(compscore)  
         print(userscore)
        elif user == s :
            if comp == p: 
             userscore += 1
             print(compscore)  
             print(userscore)
            elif comp == r:
             compscore += 1
             print(compscore)  
             print(userscore)
        elif user == s :
            if comp == p:
             compscore += 1
             print(compscore)  
             print(userscore)
            elif comp == s:
             userscore += 1
             print(compscore)  
             print(userscore)
             
    i += 1
    if i == 10 :
     break
 
  
print( userscore )
print( compscore )

if userscore < compscore :
    print("Computer Wın !!")

elif userscore == compscore :
    print("Game is TIE !!")
else:
    print("You WIN!!!")