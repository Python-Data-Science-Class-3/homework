# Body Mass Index Calculator


bodymass = int(input ("Enter your weight : ")) 

height = float(input ("Enter your height :"))
ratio  = bodymass/height**2
#If we divide it by its square,
# the body mass index is obtained
if ratio <25:
    print("weight is normal") #result by taking the length is below 25, NORMAL
elif ratio <30 and ratio > 25 : #if it is between 25-30
    print("OVER WEIGHT")
elif ratio < 40 and ratio >30 :
    print("OBSE") # if 30-40
elif ratio > 40 : #if 40 
    print("EXTREMELY OBSE ")
