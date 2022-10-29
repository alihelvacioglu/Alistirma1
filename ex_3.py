s = 0
for i in range (1,999):
    a = 1
    for b in range (1,i):
        a *= b
    s += 1/a
print(s)