#https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)

#https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())

for n in range(1, n+1):
    print(n, end ="")

#https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())

for n in range(n):
    print(n**2) 

#https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)

#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    result = ''
    for i in s: 
        if i.islower():
            result += i.upper()
        elif i.isupper():
            result += i.lower()  
        else:
            result += i     
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)