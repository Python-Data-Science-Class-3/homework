


def alfabetich_order(mylist):

    '''
    This function sort input words and write it back.
    '''
    a=mylist.split('-')
    a=sorted(a)
    y=[]
    for i in a:
        y.append(i)
        y.append('-')
    y.pop()
    print(y)

mylist = input("write some word:\n")
alfabetich_order(mylist)
