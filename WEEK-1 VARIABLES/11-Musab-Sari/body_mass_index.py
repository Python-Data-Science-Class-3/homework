'''
Developer   : Musab SARI
Date        : 06.12.2022

Application : Body Mass Index Calculation and Comparison

Explanation : Body Mass Index(BMI) is a subjective index that has parameters of weight and height. 
The index is assigned to certain intervals and puts people in 4 main categories which are normal, over weight, obese, extremely obese.
'''

Name = input("Name:") # user input for name
Surname = input("Surname:") # user input for surname
weight = float(input("Weight in kg:")) # user input for wight in kilogram
height = float(input("Height in centimetre:")) # user input for heigt in centimeter

body_mass_index = weight/((height/100)**2) # BMI calculation, heigt is converted to meter

print(f'{Name} {Surname}', 'your body mass index is %3.2f' %body_mass_index) # Output of index for the user, exhibits only two digits after coma

if body_mass_index < 25: # output function for main categories
    print("Normal")

elif body_mass_index >= 25 and body_mass_index < 30:
    print("Over Weight")

elif body_mass_index >= 30 and body_mass_index < 40:
    print("Obese")

else:
    print("Warning! Extremely Obese")