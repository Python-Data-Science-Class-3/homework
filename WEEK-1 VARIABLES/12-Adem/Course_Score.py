# mg midterm grade, fg final grade

sname, ssurname, snum =input("Enter the student's name, surname and number, leaving a space between them.").split()
les1, les2, les3, les4 = input("Enter the names of the 4 courses , leaving a space between them.").split()
mg1, mg2, mg3, mg4 = input(f"Enter midterm grade in oerder of {les1},{les2},{les3},{les4}").split()
fg1, fg2, fg3, fg4 = input(f"Enter final grade in oerder of {les1},{les2},{les3},{les4}").split()
avarage1=round((float(mg1)*0.4+ float(fg1)*0.6),2)
if avarage1>=50:
   print(les1,"avarage:",avarage1,"PASSED")
else: print(les1,"avarage:",avarage1,"FAILED")
avarage2=round((float(mg2)*0.4+ float(fg2)*0.6),2)
if avarage2>=50:
   print(les2,"avarage:",avarage2,"PASSED")
else: print(les2,"avarage:",avarage2,"FAILED")
avarage3=round((float(mg3)*0.4+ float(fg3)*0.6),2)
if avarage3>=50:
   print(les3,"avarage:",avarage3,"PASSED")
else: print(les3,"avarage:",avarage3,"FAILED")
avarage4=round((float(mg4)*0.4+ float(fg4)*0.6),)
if avarage4>=50:
   print(les4,"avarage:",avarage4,"PASSED")
else: print(les4,"avarage:",avarage4,"FAILED")