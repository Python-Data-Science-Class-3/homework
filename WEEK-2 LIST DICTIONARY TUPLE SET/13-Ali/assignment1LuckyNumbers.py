while True:
    n = int(input('Enter a number to find lucky number for it: '))
    sequence1 = [in_range for in_range in range(1, n + 1)]
    print(sequence1)
    print("len is", len(sequence1))
    a = []
    aa = 2
    while aa <= len(sequence1):  #in this step determine of elements disappearing is accomplished. 
        for i in range(len(sequence1)):
            if  i % aa == aa -1:
                a.insert(len(a),sequence1[i]) # here, they are accumulated in a list 
        for ii in a:
            sequence1.remove(ii)             # so that here they are removed from main list.
        
        print(sequence1, 8*' ', str(aa)+"th element desappered last time and", "new length:",str(len(sequence1))+'!')
        a = []
        aa += 1        
    
