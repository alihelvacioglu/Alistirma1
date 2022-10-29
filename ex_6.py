from itertools import count


a = 0
for i in range(1000,10000):
    if int(str(i)[0]) > int(str(i)[3]):
        a += 1
        print(i)
result=count(a)
print(result)


