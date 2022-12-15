#Sequential multiplication table of numbers from 1 to 10
#The locations of i and j in the print function are very important because i loops up to 10 
# and j loops from 1 to 5 and 5 to 10. So I realized we have to write it as j x i.
#  If you think with reverse logic, the solution will be easier.


for i in range(1, 11):
    for j in range(1, 6): 

        print(f'{j:3}  x{i:3} = {i * j:3}   ', end= "  | ") #With the last method, we printed the first 5 lines of numbers 
                                                            #side by side and in between with a line.
        if j == 5:                                          # When I reached the last element, I made the transition to the bottom line.
            print()
print()
for i in range(1,11):                                       
    for j in range(6,11):                                     #For the other part, this time we counted 5 times, starting from the 6th element.
        print(f' {j:3}  x{i:3} = {i * j:3}  ', end= "  | ")  #This part is very important because the process is done 
                                                            #here with the end function and the position of i and j.
        if j == 10:
            print()
