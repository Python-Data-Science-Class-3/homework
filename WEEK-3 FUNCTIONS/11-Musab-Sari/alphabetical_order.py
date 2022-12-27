'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Alphabetical Order

Explanation : Alphabetical order is an application where user can enter multiple words at the same time with a '-' between them and outputs sorted
version of the same items in the list with '-' in between them.
'''
alphabetical_order = lambda x = sorted(map(str, input('Please enter your words with an expression "-" in between them:').split('-'))): print('-'.join(x))

alphabetical_order()