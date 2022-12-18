liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21,22] 
count = 1
for x in range(0, len(liste)):
    if len(liste) <= count:
        break
    liste.remove(liste[count]) 
    count = count+1
secondCount = 2  
#[1,3,5,7,9] 
for x in range(0, len(liste)):
    if len(liste) <= secondCount:
        break
    liste.remove(liste[secondCount]) 
    secondCount = secondCount+2   
#[1,3,7,9]
thirdCount = 3
for x in range(0, len(liste)):
    if len(liste) <= thirdCount:
        break
    liste.remove(liste[thirdCount]) 
    thirdCount = thirdCount+3  
#[1,3,7]
print(liste)