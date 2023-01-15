"""Course Score Calculation
User Name, Surname, Student Number, 4 course names, Visa and Final grades will be required. 
The sum of 40% of the midterm grade and 60% of the final grade will give the year-end average. 
If the average is less than 50, “FAILED” on the screen, 50 and above, “PASSED” will be printed on the screen. 
This printing process is in 4 lessons. will be done and the lessons will be written one after the other.
"""

name = input("Name: ")
surname = input("Surname: ")
s_number = input("Student Number: ")
print("\n")

#to take inputs for each courses for whatever number of courses are needed: for loop
for i in range(1,5):
    courses = input(f"Course {i}: ")
    visa = int(input("Visa: "))
    final = int(input("Final: "))
    print("\n")

#Year-end average is calculated by 40% of visa and 60% of final grade. The result will be in type "0,00".

    average = visa*40/100 + final*60/100
    average= round(average,2)

    print(f"Year-end average for {courses} is {average}")

    if average < 50:
        print(f"{courses} FAILED")
    elif average >= 50:
        print(f"{courses} PASSED")
