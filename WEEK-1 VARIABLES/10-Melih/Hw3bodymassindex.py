""" 
Developer : Melih Orhan Yilmaz
Date      : 06.12.2022

Application : Body Mass Index Calculator

Explanation : Parameter showing whether a person's weight is normal for their height. It is called Body Mass Index. 
In short, a person's weight is equal to a person's height. If we divide it by its square, the body mass index is 
obtained. User's weight and height If the result by taking the length is below 25, NORMAL, if it is between 25-30 
OVER WEIGHT, OBSE if 30-40, EXTREMELY OBSE if 40 and over print a warning.

 """

height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))
BMI = weight / ((height/100)**2)
print(f"Your Body Mass Index is {BMI}")

if BMI < 25:
    print("NORMAL")
elif BMI < 30:
    print("OVER WEIGHT")
elif BMI < 40:
    print("OBSE")
else:
    print("WARNING!!! EXTREMELY OBSE")
