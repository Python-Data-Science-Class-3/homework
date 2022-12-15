height,weight = input(f"Enter your height (m) and weight (kg), leaving a space between them.").split()
cal = abs(round((float(weight)/ pow(float(height),2)),2))
if cal<25:
    print("body mass index", cal,"NORMAL")
elif cal<30:
    print("body mass index", cal,"OVER WEIGHT")
elif cal<40:
    print("body mass index", cal,"OBSE")
elif cal>=40:
    print("body mass index=", cal,"EXTREMELY OBSE")

