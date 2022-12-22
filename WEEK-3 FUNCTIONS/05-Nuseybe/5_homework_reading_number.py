#Write a function that outputs the transcription of an input number with two digits.
#Example: 28---------------->Twenty Eight
#written by Nuseybe at 20.12.2022


num=input("Write a number 10 to 100:  ")                               #entering a number
inp=list(num)
num_list1=['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteeen','Seventeen','Eighteen','Nineteen']  #The list created due to the writing difference of the numbers 10-19
num_list2=['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']              # the list created for 2. digit
num_list3=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']                      #the list created for 1. digit
i=0
x=int(inp[0])                                             #making index 0 for 1. digit
y=int(inp[1])                                             #making index 1 for 2. digit
def write_num(x,y):
    global i
    while i in range (i,10):
        if x==1 and y>=i : print(f"{num}-----> {num_list1[y]}")     #list1 are used when 2. digit is equal 1
        if x==1:                    
            break
        elif x>1: print(f"{num}-----> {num_list2[x-2]} {num_list3[y-1]}")               #list2 and list3 are used when 2. digit is greater than 1
        break

write_num(x,y)