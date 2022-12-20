
'''
This program finds the frequency of letters in a text

'''
text = input("Enter a sentence : ")
dic = {}
for letter in text:
    if letter not in dic :
        dic[letter.lower()] =1  # eger dic te  degilse ekliyoruz
    else :
        dic[letter.lower()] += 1 # eger key dic te ise valuesini 1 artiriyoruz
print(dic)