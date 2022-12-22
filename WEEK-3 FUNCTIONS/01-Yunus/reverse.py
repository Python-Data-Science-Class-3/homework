

def reverse():
    '''
    This function write a word in reversed way

    '''

    a=input("Enter a word : \n")
    a=a.split(', ')

    for i in a:
        b=i[::-1]
        if i==b:
            print(True,end=', ')
        else:
            print(False,end=', ')


reverse()
