'''Developer : Tuba GÜMÜS ESMEK
   Date      : 22.12.2022
   Subject   : Perfect Number

'''
#Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
#The smallest perfect number is 6, which is the sum of 1, 2, and 3.
#Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
#Write a function that finds perfect numbers between 1 and 1000. 
# #Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.



from functools import  reduce

def diving_numbers(num):  #creating the function
    sum=0                 
    for i in range(1,num): 
        if num%i == 0:        
            sum=sum+i       
    if sum==num:         # eger perfect number ise return yap    
        return sum



# res = reduce(lambda x,y : x+y, )
# print(diving_numbers(1000)) 

div_list = list(filter(diving_numbers,range(1,1001)))
'''
bu fonksiyona 1000 kere gidip return olarak perfect number i filter ile alip listeye ceviriyor.
elimizde perfect numberlardan olusan bir liste var.
'''
print(f"{reduce(lambda x,y: x+y,div_list)}") # elimnizde div_list var ve icindeki degerleri reduce ile toplayalim.

# print(f"{reduce(lambda x,y: x+y,list(filter(diving_numbers,range(1,1001))))}") # birlestirip tek satirda yazdik


'''
Ornek reduce()

from functools import reduce
sayilar = [1, 3, 5, 7, 9]
toplam = reduce (lambda x, y : x +y, sayilar )
print( toplam )

'''    
