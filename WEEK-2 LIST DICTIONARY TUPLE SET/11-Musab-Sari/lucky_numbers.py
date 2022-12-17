'''
Developer   : Musab SARI
Date        : 13.12.2022

Application : Lucky Numbers

Explanation : Lucky numbers is an application where you can create a list and see the survivors from that list which are called lucky numbers.
Survival process is defined as follows, at the first phase, every second element from the list is removed and at the second phase, every third element is removed
and it goes on like this till there is no possible iteration left.
'''

n = list([x for x in range(1, int(input('Enter the range of your list:')) + 1)])#to create list 

print('Your list = ', n)

for i in range(2, len(n)):
    
    if i < len(n):
        del n[(i - 1)::(i)] 
    else:
        break

print('Your lucky numbers = ', n)