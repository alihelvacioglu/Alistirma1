for i in range(10000,100000):
    s=0
    for d in range(2,317):
        if i%d == 0:
            s+=1
    if s == 0:
        print(i)            
               
