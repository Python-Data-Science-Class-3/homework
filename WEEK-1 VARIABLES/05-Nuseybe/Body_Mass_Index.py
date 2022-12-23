user_height = input ("Please enter your height :")
us_height=float (user_height)
user_weight = input ("Please input your weight :")
us_weight=float (user_weight)
Bmi= (us_weight/((us_height/100)*(us_height/100))) #Bmi(Body_Mass_Index)
if Bmi<=20.5 and  Bmi >=18.5 :
    print (f"Your Bady Mass Index {Bmi:.2f}, Normal")
elif Bmi>25 and Bmi<=30 :
    print(f"Your Bady Mass Index {Bmi:.2f}  Over Height")
elif Bmi>30 and Bmi<=40 :
    print(f"Your Bady Mass Index {Bmi:.2f}  Obse")
elif Bmi >40 :
    print(f"Your Bady Mass Index {Bmi:.2f}, Extremly Obse")