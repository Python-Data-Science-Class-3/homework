

#Hacerrank odevleri
#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

N = int(input())
L =[]
for comands in range(1,N+1):
    i = input()
    newList = i.split(' ')
    if newList[0].lower() == "insert":
        L.insert(int(newList[1]),int(newList[2]))
    elif newList[0].lower() == "print":
        print(L)

    elif newList[0].lower() == "remove":
        L.remove(int(newList[1]))

    elif newList[0].lower() == "append":
        L.append(int(newList[1]))

    elif newList[0].lower() == "sort":
        L.sort()

    elif newList[0].lower() == "pop":
        L.pop()
    elif newList[0].lower() == "reverse":
        L.reverse()


   
      # https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true 


n = int(input())
t = tuple(map(int,input().split(' ')))
print(hash(t))


#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true



n = int(input())
s = set(map(int, input().split()))
a = int(input())
# command = list(map(str,input().split(' ')))
for i in range(0,a):
    command = list(map(str,input().split(' ')))
    if command[0].lower() == "pop":
        if len(s) == 0:
            pass
        else :
            s.pop()
    if command[0].lower() == "discard":
        s.discard(int(command[1]))
    if command[0].lower() == "remove":
        s.remove(int(command[1]))
   
print(sum(s))



#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true


n = int(input())
country = set()
for i in range(0,n):
    country.add(input())
print(len(country))
