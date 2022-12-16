"""Program for shifting elements in a list. The user will be entered for the 
   highest element of the list. Shifting number will be entered"""
S_list = int(input("Enter the upper limit of the lucky numbers"))
S_num = int(input("Enter the upper limit of the lucky numbers"))
#making list
S_list = [i for i in range(1,S_list+1)]
print (S_list)
#Warn when the scroll number is more than the number of elements of the list
if S_num >= len (S_list):
        print("The shifting number cannot be same or more from the number of elements of the list. Try again")
        print("Number of elements of the list :", len(S_list))
        print("Number of shifting :",S_num)
else: #shifting numbers with slicing method
    S_list = S_list[S_num:] + S_list[:S_num] 
    print(S_list)   