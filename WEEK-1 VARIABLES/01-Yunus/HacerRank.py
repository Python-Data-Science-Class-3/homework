# https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
a = int(input())
b = int(input())
print(a//b)
print(a/b)

# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
a = int(input())
b = int(input())



print(a+b)
print(a-b)
print(a*b)

# https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    for i in range(1,(n+1)):
        print(i,end= '')



# https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true

n = int(input())
for i in range(0,n):
    print(i**2)

# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    modified = ''
    for letters in s :
        if letters==letters.upper():
            letters= letters.lower()
        elif letters == letters.lower():
            letters = letters.upper()
        else :
            letters = letters
        modified += letters
    return modified

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)