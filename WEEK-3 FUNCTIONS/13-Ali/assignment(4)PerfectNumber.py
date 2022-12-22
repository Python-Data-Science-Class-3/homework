# ## 4-perfect_number.py
# Perfect number: Perfect number is a positive
# integer that is equal to the sum of its 
# proper divisors.
# The smallest perfect number is 6, which is
# the sum of 1, 2, and 3.
# Some other perfect numbers are 28(1+2+4+7+14=28),
# 496 and 8128.
# Write a function that finds perfect numbers
# between 1 and 1000. Check perfect numbers
# between 1 and 1000 and find the sum of the
# perfect numbers using reduce and filter 
# functions.

def gist(caption):
    pile = []
    for antecedent in range(1,caption):
        if caption % antecedent == 0:
            pile.append(antecedent)
    if caption == sum(pile):
        return True
    else:
        return False        


sumPerfect = filter(lambda sayi: gist(sayi)== True, range(1,1000))
listPerfect = list(sumPerfect)

print("perfect numbers between 1 to 1000: ", listPerfect)
print("sum of perfect numbers between 1 to 1000: ",sum(listPerfect))
