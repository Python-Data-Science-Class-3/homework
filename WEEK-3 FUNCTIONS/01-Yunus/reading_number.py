


def reading_number():

    '''
This function read the number from user.
'''

    tens = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    numbers =["zero","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]            
    while True:
        n = input("Enter a number between 0-99 : \n")
        l = list(n)
        a = int(l[0])
        if int(n)<10:
            print(numbers[a])
        else :
            b = int(l[1])

            if 10<int(n)<20:
                print(f"{teens[b]}")
            elif b == 0:
                print(f"{tens[a-1]}")
            else :
                print(f"{tens[a-1]} {numbers[b]}")
reading_number()