'''
Developer   : Musab SARI
Date        : 06.12.2022

Application : Course Score Calculation

Explanation :  'Course score calculation' is prepared for students who have courses consisting only one midterm and final which having weights of 40% and 60%.

'''

User_Name = input("User name:") # inputs for user  
Surname = input("Surname:")
Student_Number = int(input("Student Number:"))
Course_amount = int(input("Enter the course amount:"))

Visa_list = [] #lists created later to store data
Final_list = []
average_list = []
course_names_list = [] 

count = 0 # to be able to create function with while loop, count variable is created

while count < Course_amount: # to make the program eligible to get limitless input from the user for course amount
    course_names = input("Course name:")
    visa = float(input("Enter your visa grade:"))
    final = float(input("Enter your final grade:"))
    
    if visa >= 0 and final >= 0 and visa <= 100 and final <= 100: # to arrange 100 based note system
        course_names_list.append(course_names)
        Visa_list.append(visa)
        Final_list.append(final)
        average = (float(Visa_list[count])*(0.4)) + float((Final_list[count])*(0.6))
        average_list.append(average)
        print(f'For {course_names_list[count]}', 'your year end average grade is %3.2f' %average_list[count])
        count += 1
    
    else:
        print("You have entered invalid value")
        continue

print(50*'~') # to make user friendly interface

for i in range(Course_amount): # Output for the courses of the user if they are passed or not
    
    if average_list[i] < 50:
        print(f'For {course_names_list[i]}', 'your year end average is %3.2f' %average_list[i],'. Sorry, you have FAILED!')
    
    else:
        print(f'For {course_names_list[i]}', 'your year end average is %3.2f' %average_list[i],'. Congratulations, you have PASSED!')        

print(50*'~') # to make user friendly interface

Average_all_courses = sum(average_list)/Course_amount # average function for all the courses of the user
print('Average of all your grades is %3.2f' %Average_all_courses) # output for all the courses in average