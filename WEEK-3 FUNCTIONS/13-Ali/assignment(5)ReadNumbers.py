# ## 5-reading_number.py
# Write a function that outputs the transcription of an input number with two digits.
# Example:
# 28---------------->Twenty Eight
while True:    
    tens= { 
        10:"Ten",
        11:"Eleven",
        12:"Twelve",
        13:"Thirteen",
        14:"Fourteen",
        15:"Fifteen",
        16:"Sixteen",
        17:"Seventeen",
        18:"Eighteen",
        19:"Nineteen",
    }   
    till9={ 
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
        0:"",
    }
    tys={
        20:"Twenty",
        30:"thirty",
        40:"Forty",
        50:"Fifty",
        60:"Sixty",
        70:"Seventy",
        80:"Eighty",
        90:"Ninety",
    }

    while True:
        try:
            entry = int(eval(input("\n enter a number with 2 digits: "))) 
            if 9 < entry < 100:
                break
            else:
                raise ValueError
        except:
            print("\n \n you can only enter a 2 digit number!!!")


    def writeNum(a):
        if entry < 20:
            print(tens[entry])
        else:
            entryStr = str(entry)
            entryInt1 = int(entryStr[0]+'0')
            entryInt2 = int(entryStr[1])
            print(str(entry)+"----------------> "\
    +str(tys[entryInt1])+"-"+str(till9[entryInt2]))
            
    writeNum(entry)

#below ist without function
# while True:
#     cardinalNum = { 
#         10:"Ten",
#         11:"Eleven",
#         12:"Twelve",
#         13:"Thirteen",
#         14:"Fourteen",
#         15:"Fifteen",
#         16:"Sixteen",
#         17:"Seventeen",
#         18:"Eighteen",
#         19:"Nineteen",
#         20:"Twenty",
#         21:"twenty-one",
#         22:"twenty-two",
#         23:"twenty-three",
#         24:"twenty-four",
#         25:"twenty-five",
#         26:"twenty-six",
#         27:"twenty-seven",
#         28:"twenty-eight",
#         29:"twenty-nine",
#         30:"thirty",
#         31:"thirty-one",
#         32:"thirty-two",
#         33:"thirty-three",
#         34:"thirty-four",
#         35:"thirty-five",
#         36:"thirty-six",
#         37:"thirty-seven",
#         38:"thirty-eight",
#         39:"thirty-nine",
#         40:"forty",
#         41:"forty-one",
#         42:"forty-two",
#         43:"forty-three",
#         44:"forty-four",
#         45:"forty-five",
#         46:"forty-six",
#         47:"forty-seven",
#         48:"forty-eight",
#         49:"forty-nine",
#         50:"fifty",
#         51:"fifty-one",
#         52:"fifty-two",
#         53:"fifty-three",
#         54:"fifty-four",
#         55:"fifty-five",
#         56:"fifty-six",
#         57:"fifty-seven",
#         58:"fifty-eight",
#         59:"fifty-nine",
#         60:"sixty",
#         61:"sixty-one",
#         62:"sixty-two",
#         63:"sixty-three",
#         64:"sixty-four",
#         65:"sixty-five",
#         66:"sixty-six",
#         67:"sixty-seven",
#         68:"sixty-eight",
#         69:"sixty-nine",
#         70:"seventy",
#         71:"seventy-one",
#         72:"seventy-two",
#         73:"seventy-three",
#         74:"seventy-four",
#         75:"seventy-five",
#         76:"seventy-six",
#         77:"seventy-seven",
#         78:"seventy-eight",
#         79:"seventy-nine",
#         80:"eighty",
#         81:"eighty-one",
#         82:"eighty-two",
#         83:"eighty-three",
#         84:"eighty-four",
#         85:"eighty-five",
#         86:"eighty-six",
#         87:"eighty-seven",
#         88:"eighty-eight",
#         89:"eighty-nine",
#         90:"ninety",
#         91:"ninety-one",
#         92:"ninety-two",
#         93:"ninety-three",
#         94:"ninety-four",
#         95:"ninety-five",
#         96:"ninety-six",
#         97:"ninety-seven",
#         98:"ninety-eight",
#         99:"ninety-nine",
#     } 
#     try:
#         searchedNum = int(input("\nplease enter an integer with \
# 1 or 2 digits to see its transcription: "))
#         print(searchedNum,"---------------->" ,cardinalNum[searchedNum])
#     except KeyError:
#         print("please enter only a NUMBER with 2 DIGITS !!!")

        
             



    

