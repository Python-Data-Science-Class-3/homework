
'''Course Score Calculation
    User Name, Surname, Student Number, 4 course names, Visa and 
    Final grades will be required. The sum of 40% of the midterm 
    grade and 60% of the final grade will give the year-end average. 
    If the average is less than 50, “FAILED” on the screen, 50 and 
    above, “PASSED” will be printed on the screen. This printing
    process is in 4 lessons. will be done and the lessons will be
    written one after the other.'''
Name = input("enter name: ")
Surname = input("enter surname: ")
while True:
    try:
        Snumber = int(eval(input("enter studen number: ")))
        #len(str(Snumber)) == 7
        break
    except NameError:
        print("Student Number can only be numaric please enter promptly")
while True:
    try:    
        visaMath = input("enter Math visa grade: ")
        finalMath = input("enter Math final grade: ")
        visaPhysic = input("enter Physic visa grade: ")
        finalPhysic = input("enter Physic final grade: ")
        visaArts = input("enter Arts visa grade: ")
        finalArts = input("enter Arts final grade: ")
        visaSocialSciences = input("enter Social Sciences visa grade: ")
        finalSocialSciences = input("enter Social Sciences final grade: ")
        if(visaMath.isdigit() and finalMath.isdigit() and visaPhysic.isdigit() and
            finalPhysic.isdigit() and visaArts.isdigit() and finalArts.isdigit() and
            visaSocialSciences.isdigit() and finalSocialSciences.isdigit()):
            visaMath = int(visaMath)
            finalMath = int(finalMath)
            visaPhysic = int(visaPhysic)
            finalPhysic = int(finalPhysic)
            visaArts = int(visaArts)
            finalArts = int(finalArts)
            visaSocialSciences = int(visaSocialSciences)  
            finalSocialSciences = int(finalSocialSciences)
        else:
            raise ValueError()

        if  (0 <= visaMath <= 100 and
            0 <= finalMath <= 100 and
            0 <= visaPhysic <= 100 and
            0 <= finalPhysic <= 100 and
            0 <= visaArts <= 100 and
            0 <= finalArts <= 100 and
            0 <= visaSocialSciences <= 100 and 
            0 <= finalSocialSciences <= 100): 
                break      
        raise ValueError()
    except ValueError:
        print("a visa or final grade can only be integer and bettween 0 and 100")
        
        

        
    
year_endMath = visaMath*0.4 + finalMath*0.6
year_endPhysic = visaPhysic*0.4 + finalPhysic*0.6
year_endArts = visaArts*0.4 + finalArts*0.6
year_endSocialSciences = visaSocialSciences*0.4 + finalSocialSciences*0.6
print(f'{Name} {Surname} {Snumber}')
print("Math Year-End Resul = {:0.2f}".format(year_endMath), end=' and ')
if year_endMath >= 50:
    print("PASSED")
else: 
    print("FAILED")   
print("Physic Year-End Resul= {:0.2f}".format(year_endPhysic), end=' and ')
if year_endPhysic >= 50:
    print("PASSED")
else: 
    print("FAILED")   
print("Arts Year-End Resul= {:0.2f}".format(year_endArts), end=' and ')    
if year_endArts >= 50:
    
    print("PASSED")
else: 
    print("FAILED")   
    
print("Social Sciences Year-End Resul= {:0.2f}".format(year_endSocialSciences), end=' and ')    
if year_endSocialSciences >= 50:
    print("PASSED")
else: 
    print("FAILED")    
        
        

        