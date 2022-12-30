#As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. 
#So that I can find the least common multiple (L.C.M.) of my inputs.

#Acceptance Criteria:
#Ask user to enter the four numbers. 
# Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs. 
# Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in module of math (use import gcd function in math)


from math import gcd

def Lcm(x,y,z,t): #define a function,we find lcm using gcd  
### it would be better to use all letters as lower! 
### Please don't use capital letters as long as not required. 
### Let's replace 'Lcm' with 'lcm'.

### what do you mean with these lines? Can you explain?
### Should we write self an algorithma, of may we use math.gcd?
### Could you please try to write an algorithma to find the least common multiple?

    L1=int((x*y)/gcd(x,y))
    L2=int((z*t)/gcd(z,t))
    L=int((L1*L2)/gcd(L1,L2))
    return L

while True:
    try:
        first_number=int(input("Enter first number:"))
        second_number=int(input("Enter second number:"))
        third_number=int(input("Enter third number:"))
        fourth_number=int(input("Enter fourth number:"))
        L=Lcm(first_number, second_number, third_number,fourth_number)
        print("The LCM Of Four Numbers:",L)
        break
    except:
        print("Oops,Type Error")

### Good done!
