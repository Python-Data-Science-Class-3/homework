#Write a programme to generate the lucky numbers from the range(n). 
# These are generated starting with the sequence s=[1,2,...,n]. 

# At the first pass, we remove every second element from the sequence, 
# resulting in s2. At the second pass, we remove every third element 
# from the sequence s2, resulting in s3, and we proceed in this way 
# until no elements can be removed. The resulting sequence are the 
# numbers lucky enough to have survived elimination. The following 
# example describes the entire process for n=22 Original sequence 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] 
# Remove 2nd elements [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
# Remove 3rd elements [1, 3, 7, 9, 13, 15, 19, 21] 
# Remove 4th elements [1, 3, 7, 13, 15, 19] Remove 5th elements [1, 3, 7, 13, 19] 
# We cannot remove every other 6th element as there is no 6th element. 
# Input 22 Output Lucky numbers are [1, 3, 7, 13, 19]

print("\n\n")  
# Burda bunu kullanmamiza gerek yok diye dusunuyorum, kullanma amacinizi bilemedim
n = int(input("Please input a number: ")) 
# Ustteki satiri burda kullanmak istemis olabilirsiniz, 
# : kullanmak yerine inputu yazinin altinda almak icin kullanabilirsiniz
list1 = list(range(1, n+1))                 # to generate the sequence as the numbers from 1 to n
                                            # print(f"Sequence:{list1}")
                                            
for k in range(2, n):
    del list1[k-1::k]                        # to remove every second, third, and number on the next alignment, by using slicing.. 
                                             # print(list1)
    if k == len(list1):                      # to break the loop when the alignment that we want to remove is equal to the length of our list:
        # if len(list1) < k: olarak kosulun kurulmasi gerekir 
        # k her zaman liste uzunluguna esit olmayabilir, ama liste uzunlugundan kucuk oldugu her durumda donguden cikabiliriz
        # yani kosul k'nin liste uzunluguna esit olmasi degil,
        # liste uzunlugunun k'dan buyuk olmasi ki boylece listeden atacak eleman kalmayip donguyu bitirsin,
        # ama esit olmasina bagli olarak kosul yazarsak silebilecegimiz eleman olmasina ragmen silmeden islemi bitiririz
        # liste uzunlugu 10 iken 'k' da  ise 
        break  # quit yerine burada 'break' kullanmamiz gerekiyor, 
        # bu haliyle kod dongu bitirme kosulunu sagladigi durumda hata veriyor

print(f"\nLucky numbers are {list1}")

'''
Gayet iyi...
'''