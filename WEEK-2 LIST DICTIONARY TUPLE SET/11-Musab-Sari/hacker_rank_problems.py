'''
Developer   : Musab SARI
Date        : 13.12.2022
'''

# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# if __name__ == '__main__':
#     N = int(input())
#     t = []
#     for i in range(N):
#         commands, *numbers = input().split()
#         if commands == 'print':
#             print(t)
#         else:
#             numbers = list(map(int,numbers))
#             a = f't.{commands}{*numbers,}'
#             eval(a)

#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# n = int(input())
# integer_list = map(int, input().split())
# t = ()
# for x in integer_list:
#     t += (x,)
# print(hash(t))

#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
# n = int(input())
# s = set(map(int, input().split()))
# N = int(input())
# for i in range(N):
#     commands = input().split()
#     if 'remove' in commands:
#         s.remove(int(commands[1]))
#     elif 'discard' in commands:
#         s.discard(int(commands[1]))
#     elif 'pop' in commands:
#         s.pop()
# print(sum(s))

#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# N = int(input())
# a = {}
# s = set(a)
# for i in range(N):
#     country = input()
#     s.add(country)
# print(len(s))