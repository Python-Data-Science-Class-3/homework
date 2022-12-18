'''
DEVOLOPER  : TUBA GÜMÜS ESMEK
DATE       : 15.12.2022 
           : SHIFTING_ELEMENTS
'''
#Write a program that takes two inputs; one of them is a list and the other is a number, and 
# returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative).
#  Use wrap-around if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.
#  Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]

new_list = list(input("please share a new list:\n")) #user creatin a list
print(new_list)
n = int(input("write a number:\n")) #choosing a number
#print(n)
new_list1 = new_list[-n:] + new_list[0:-n] #define the new list
#)
if n > 0:
     new_list1 = new_list[-n:]+new_list[:-n] #returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative).
     #print(new_list1)


print(new_list1)