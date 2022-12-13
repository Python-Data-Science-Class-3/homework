
print("Body Mass Index Calculator")
weight=int(input("enter your weigt"))
height=float(input("enter your height"))
index=(weight)/(height*height)

print("result:",index)
if(index<25):
   print("Normal")
elif(index>=25) and (index<30):
   print("Over Weight")
elif(index>=30) and (index<40):  
   print("Obse")
else:
   print("Extremely Obse")
