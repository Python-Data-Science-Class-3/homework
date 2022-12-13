'''3. Body Mass Index Calculator
    Parameter showing whether a person's weight is normal for their
    height. It is called Body Mass Index. In short, a person's weight 
    is equal to a person's height. If we divide it by its square, the
    body mass index is obtained. User's weight and height If the 
    result by taking the length is below 25, NORMAL, if it is between 
    25-30 OVER WEIGHT, OBSE if 30-40, EXTREMELY OBSE if 40 and over
    print a warning.'''
while True:
    while True:
        try:
            length = float(eval(input("Enter yor length in centemeter: ")))    
            weigth = float(eval(input("Enter yor weigth in kg: ")))    
            break
        except NameError:
            print("length and weigth can be entered only numeric ")
    body_mass_index = weigth/((length/100)**2)
    print("Your Body Mass Index is: {:0.2f}".format(body_mass_index))

    if body_mass_index < 25:
        print("NORMAL")
    elif 25 <= body_mass_index <= 30:
        print("OVER WEİGHT")
    elif 30 < body_mass_index <= 40:
        print("OBSE")
    else:
        print("EXTREMELY OBSE")
    
    
    
    
    
    
    
    
    
    
    