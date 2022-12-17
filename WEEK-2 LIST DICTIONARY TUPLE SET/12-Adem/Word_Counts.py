#Calculation of letter numbers of the entered sentence
a = str( input("Enter the sentence")).lower()
print (a)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#Search each letter within the alphabet 
for i in alphabet: 
#For not print letters that are not in the entered sentence and take the value "0"
    if a.count(i) > 0:
        print (tuple((i  , a.count(i))))