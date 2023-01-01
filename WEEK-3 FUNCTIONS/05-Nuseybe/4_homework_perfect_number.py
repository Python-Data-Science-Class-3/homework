#Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
#The smallest perfect number is 6, which is the sum of 1, 2, and 3.
#Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
#Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
#written by Nuseybe at 21.12.2022
def find_div(a): 
    return [b for b in range(1, int(a / 2) + 1) if a % b == 0]    #find the divisors of numbers
#print(find_div(28))

def perfect_numbers(i,j): 
    return [a for a in range(i,j+1) if sum(find_div(a)) == a]           # find the perfect numbers between two numbers


print("These are perfect number 1 till 1000: ", perfect_numbers(1, 1000))   #printing the perfect numbers which is perfect_numbers function find are
print("This is sum of perfect numbers which are 1 till 1000 : ", sum(perfect_numbers(1,1000)))  #printing the sum of perfect numbers which is 1 till 1000
