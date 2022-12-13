""" 
Developer : Melih Orhan Yilmaz
Date      : 07.12.2022

Application : Multiplication Table

Explanation : Print the multiplication table side by side

 """

for i in range(1,11): 
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}', end="    ")
    print('\n')