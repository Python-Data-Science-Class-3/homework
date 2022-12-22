


def super_number():
    '''
This is function finds super numbers

'''
    b=0
    for i in range(1,1000):
        for j in range(1,i):
            if (i)%(j)==0 and i != j :
                b=b+j
                
        if b==i :
            print(b)
        b = 0        
super_number