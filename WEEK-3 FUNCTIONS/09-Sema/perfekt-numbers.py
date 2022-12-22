def perfekt(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

#num=int(input("Please enter a number:"))

if num==perfekt(num):
    print("Number is perkekt")
else:
    print("Number is not perfekt")

def perfekt_search():
     global i
print( filter(lambda num:num%i==0,(1,1000)))