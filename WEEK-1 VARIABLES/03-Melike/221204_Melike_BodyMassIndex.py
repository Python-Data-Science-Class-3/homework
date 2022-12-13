print("Welcome to the Body Mass Index Calculator")

#to take the question again after completed one calculation: while loop
while True:
    weight = float(input("\nWeight in kg: "))
    height = float(input("\nHeight in cm: "))

    print("\nCalculating...\n")
    #height is devided by 100, since the input is in cm not meters.
    index = weight / ((height/100)**2)
    #to take the result in type of "0,00":
    index = round(index,2)
    print(f"Your body mass index is {index}")

    if index >= 40:
        print("You're EXTREMELY OBESE!!!")
    elif index >= 30:
       print("You're OBESE!!")
    elif index >= 25:
       print("You're OVER WEIGHT!")
    elif index < 18.5:
        print("You're UNDERWEIGHT!")
    else:
        print("You're HEALTHY")