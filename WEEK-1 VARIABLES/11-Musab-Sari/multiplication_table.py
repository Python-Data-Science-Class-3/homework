'''
Developer   : Musab SARI
Date        : 06.12.2022

Application : Multiplication table 

Explanation : Multiplication table, specially arrenged for better user interface and visualization
'''

for a in range(1,11): # this for block is for the first 5 column
    
    for b in range(1,11):
        
        if b == 6 and a in range(11):
            print('')
            break
        print(f'{b} * {a:>2} = {b*a:>3}', end='\t')

print(77*'-') # to make user friendly interface

for a in range(1,11): # this for block is for the last 5 column
    
    for b in range(6,12):
        
        if b == 11 and a in range(11):
            print('')
            break
        print(f'{b} * {a:>2} = {b*a:>3}', end='\t')