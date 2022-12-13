name = input("Name:")
surname = input ("Surname:")
snummer = input("Student Nummer:")
course1 = input("Course 1")
course2 = input("Course 2")
course3 = input("Course 3")
course4 = input("Course 4")
i = 1 
while True :
    visa = input (f"Visa {i}")
    final = input (f"Final {i}")
    if i == 1 : 
        visa1=float(visa)
        final1= float(final)
    elif i == 2 :
        visa2 = float(visa)
        final2= float(final)
    elif i == 3 :
        visa3= float(visa)
        final3= float(final)
    else :
        visa4 = float(visa)
        final4 = float(final)
    i += 1
    if i == 5 :
     break

course1ave=((visa1*40)/100 +(final1*60)/100)
course2ave=((visa2*40)/100 +(final2*60)/100)
course3ave=((visa3*40)/100 +(final3*60)/100)
course4ave=((visa4*40)/100 +(final4*60)/100)
print(f" Name : {name} \n Surname : {surname} \n Student Nummer : {snummer} \n Course 1 : {course1} \n Course 2 : {course2} \n Course 3 : {course3} \n Course 4 : {course4} \n" )
if course1ave >= 50 :
    print(f"{course1} Year End Average : {course1ave:.2f}   PASSED")
else :
    print(f"{course1} Year End Average : {course1ave:.2f}   !!FAILED!!")
if course2ave >= 50 :
    print(f"{course2} Year End Average : {course2ave:.2f}   PASSED")
else :
    print(f"{course2} Year End Average : {course2ave:.2f}   !!FAILED!!")
if course3ave >= 50 :
    print(f"{course3} Year End Average : {course3ave:.2f}   PASSED")
else :
    print(f"{course3} Year End Average : {course3ave:.2f}   !!FAILED!!")
if course4ave >= 50 :
    print(f"{course4} Year End Average : {course4ave:.2f}   PASSED")
else :
    print(f"{course4} Year End Average : {course4ave:.2f}   !!FAILED!!")