#Course Score Calculation


name_surname = input("Enter your first and last name ="). upper()
student_number = int(input("Enter your school number = "))

lessons ={}  # we created a dictionary here

for i in range(4) : #We ran a request that repeated 4 times
   
    lesson = input(" Enter the name of your course =")
    visa = int(input("Enter your visa grade = "))
    final = int(input("Enter your final grade "))
    lesson_points = (visa*0.40) + (final*0.60)
    #We finalized the status of the student depending on the condition.

    if lesson_points > 50 :
        lessons.update({lesson :"   you passed"}) #Here we have added the results to the dictionary.
        
    else :
        lessons.update({lesson :"   you failet"}) #Here we have added the results to the dictionary.

    
#With a new for loop, we took values in the items in the dictionary.
for lesson, status in lessons.items():  
    print(f"lesson {lesson}  latest status{status}")
