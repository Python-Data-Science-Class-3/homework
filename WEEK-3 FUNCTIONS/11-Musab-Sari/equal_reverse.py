'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Equal Reverse

Explanation : Equal reverse is an application where user inputs range of words with a coma between them to be checked 
if they are equal to their reverse order and outputs True and False boolean values respectively.
'''
a = list(map(str, input('Please enter your words which are going to be checked if they are equal to their reverse with a coma in between them:').split(',')))

reverse_order = lambda x: [print(True) if x[i][:]==x[i][::-1] else print(False) for i in range(len(x))]

reverse_order(a)