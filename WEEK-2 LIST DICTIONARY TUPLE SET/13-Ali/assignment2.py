while True:
    while True:
        try:
            m = int(eval(input('enter a number')))
            arr1 = int(eval(input('enter only integer with at liest two digit: ')))
            # arr1 >= 10
            break
        except:
            print("please enter only enteger")
    abs(arr1)      
    arr = str(arr1)
    n = m % len(arr) 
    list1 = list(arr)
    print(list1)
    # # list1 = list(arr)
    print(list1)
    print(n)
    k = n
    if m < 0:
        while 0 < n:
            list1.insert(len(list1),list1[0])    
            del list1[0] 
            n -= 1
        print(f"list has moved {k} times to left")
        
        print(list1)
    if 0 < m:
        while 0 < n:
            list1.insert(0,list1[len(list1)-1])    
            del list1[len(list1)-1]            
            n -= 1
        print("list has moved {} times to right".format(k))
        
        print(list1)        
        