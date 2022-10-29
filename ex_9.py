
for i in range(1,1000):
    if i<9:
        print(i,end=" ,")
    elif 9<i<99 and int(str(i)[0])+ int(str(i)[1])<9:
        print(i,end=" ,")
    elif 99<i<1000 and int(str(i)[0])+int(str(i)[1]) + int(str(i)[2]) < 9:
        print(i,end=" ,")


    
        
   