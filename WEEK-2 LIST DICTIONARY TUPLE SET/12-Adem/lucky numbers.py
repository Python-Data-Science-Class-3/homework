#Program to find lucky numbers
#We set the upper limit by asking for a number of entries.
x = int(input("Enter the upper limit of the lucky numbers"))
lucky_number = [i for i in range(1, x+1)]
count = 2
print(lucky_number)
#Deletion of lucky number elements in order starting from 2

while count <= len(lucky_number):

        del lucky_number[count-1::count]
        lucky_number = lucky_number  # assignment of new lucky number
        # farkli bir listeye atasaydiniz, boyle bir esittir ile kullanabilirdiniz,
        # fakat iki ayni listeyi esitlemeniz hic bir seyi degistirmez

        count += 1  # we increase the delete interval by "1"
        
print("The lucky numbers are",lucky_number)

'''
Algoritma basarili, while dongusu ile kurmaniz cok guzel,
tebrikler
'''