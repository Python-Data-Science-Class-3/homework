""" 
Developer : Melih Orhan Yilmaz
Date      : 05.12.2022

Application : Course Score Calculation

Explanation : User Name, Surname, Student Number, 4 course names, Visa and Final grades will be required. 
The sum of 40% of the midterm grade and 60% of the final grade will give the year-end average. 
If the average is less than 50, “FAILED” on the screen, 50 and above, “PASSED” will be printed on the screen. 
This printing process is in 4 lessons. will be done and the lessons will be written one after the other.

 """

name = input('Enter your name: ')
surname = input('Enter your surname: ')
studentNumber = int(input("Enter your student number: "))
courseNumber = 0

while (courseNumber != 4):
    courseName = input('Enter your course name: ')
    visaGrade = float(input('Enter your visa grade: '))
    finalGrade = float(input('Enter your final grade: '))
    totalGrade = visaGrade * 4/10 + finalGrade * 6/10
    print(f"Course Name: {courseName}\nTotal Grade: {totalGrade}".upper())
    courseNumber += 1

    if totalGrade >= 50:
        print("PASSED")
    else:
        print("FAILED")