"""4- Mis Calculator As a user, I want to use a program which can calculate basic mathematical operations. 
So that I can add, subtract, multiply or divide my inputs.

Acceptance Criteria: The calculator must support the Addition,
Subtraction, Multiplication and Division operations. Define four functions in four files for each of them,
with two float numbers as parameters. To calculate the answer, 
use math.ceil() and get the next integer value greater
than the result Create a menu using the print command with the respective options and take an input choice from the user.
Using if/elif statements for cases and call the appropriate functions.
Use try/except blocks to verify input entries and warn the user for incorrect inputs.
Ask user if calculate numbers again. To implement this, take the input from user Y or N.
(use import sys, ceil function in math)"""
import sys
import math
from math import ceil

def hesapla():
    
    try: 
        i=math.ceil(int(input("birinci sayiyi giriniz:")))
        j=math.ceil(int(input("ikinci sayiyi giriniz:"))) 
        def topla(i,j):
            return i+j
        def cikar(i,j):
            return i-j
        def carp(i,j):
            return i*j
        def böl(i,j):
            return i/j
        if i >=j:
            raise ValueError("2.sayi birinci sayidan buyuk olmalidir!")
        elif j==0:
            raise ZeroDivisionError("bolen sayi 0 olamaz!")
    except ValueError:
        print("2.sayi birinci sayidan buyuk olmalidir!")    
    except ZeroDivisionError:
        print("bolen sayi 0 olamaz!")   
    else:
        print("tanimlanamayan hata!")
        
def tekrar():
    tekrar_hesapla=input("""devam etmek ister misiniz?
    evet icin E hayir icin H giriniz""") 
    if tekrar_hesapla.upper()=='E':
        hesapla()
    elif tekrar_hesapla.upper()=='N':
        print('Hoscakalain.')
    else:
        tekrar() 
hesapla()           