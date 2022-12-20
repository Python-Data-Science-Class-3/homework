
'''
This program returns the list obtained by shifting the elements in the list
 n places to the right (left) when n is positive (negative).
'''

a = int(input("Shift number : "))
lst = [n for n in range(1,10)]
lst2 = lst[a:]   
lst3 = lst[0:a]
lst4 = lst2 + lst3
print(lst4)