


def unrepeated(x):
    '''
This function removes repeated elements from a list
'''
    new_set = set(x)
    print(sorted(new_set))
x = input("Enter a list : ")
unrepeated(x)

'''
OR
'''

# def un_repated(x):
#     for i in range(0,len(x)-1):
#         for j in range(0,len(x)-1):
#             if x[i] == x[j] and i != j:
#                 del x[j]
#     print(x)
# x = list(input("Enter a list : \n"))
# un_repated(x)
