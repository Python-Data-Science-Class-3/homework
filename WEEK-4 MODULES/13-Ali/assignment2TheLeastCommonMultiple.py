
'''2 - The Least Common Multiple
As a user, I want to use a program which can calculate the least 
common multiple (L.C.M.) of four numbers. So that I can find the 
least common multiple (L.C.M.) of my inputs.
Acceptance Criteria:
Ask user to enter the four numbers. Use try/except blocks to verify
input entries and warn the user for Nan or non numerical inputs. 
Calculate the least common multiple (L.C.M.) of four numbers Use 
gcd function in module of math (use import gcd function in math)'''
#here first it has been chosen without lcm module 
from functools import reduce
primeNum = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
            59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
            127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 
            191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
            257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
            331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
            401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
            467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 
            563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 
            631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
            709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
            797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
            877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 
            967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 
            1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 
            1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 
            1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 
            1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 
            1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 
            1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 
            1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 
            1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 
            1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669,
            1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753,
            1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 
            1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 
            1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 
            2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 
            2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141,]
while True:
    try:
        a = int(input("first of four numbers to find out LCM of them: "))
        b = int(input("second of four numbers to find out LCM of them: "))
        c = int(input("third of four numbers to find out LCM of them: "))
        d = int(input("fourth of four numbers to find out LCM of them: "))
        if a != 0 and b != 0 and c != 0 and d != 0:
            break
        else:
            raise Exception 
        # assert a > 0 and b > 0 and c > 0 and d > 0
    except Exception:
        print("please enter integers defferent from zero!!!")
    except ValueError:
        print("please enter integer to determine LCM of them!!!")

def lcm(x,y,z,t):
    quotient = []
    LCM = []
    for i in primeNum:
        if x % i == 0: # chosen here prime numbers which evenly divisable
            xx = x
            while xx % i == 0: # here its devieded till not to divide chosen prime number
                xx /= i  #so that last quotiont is seen that can not divides 
            quotient.append(x/xx) # and it gives how many times divides prime num our mumber
        if y % i == 0:       
            yy = y
            while yy % i == 0:
                yy /= i
            quotient.append(y/yy)
        if z % i == 0:
            zz = z
            while zz % i == 0:
                zz /= i
            quotient.append(z/zz)
        if t % i == 0:
            tt = t
            while tt % i == 0:
                tt /= i
            quotient.append(t/tt)
        if quotient != []:
            LCM.append(max(quotient)) # here the most number multiple of prime which devides at list of our numbers is added to a list.
        quotient = [] 
    return LCM   
result1 = reduce((lambda x, y: x * y), lcm(a,b,c,d))
print(f"LCM of given numbers is: {int(result1)}")
# it works with lcm module below
from math import gcd, lcm

print("LCM of given numbers is:", lcm(a,b,c,d))


