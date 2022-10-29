from pickle import TRUE


def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return TRUE
a= int(input("enter a number: "))
if prime(a):
    print(a,"is a prime number")
else:
    print(a,"is not a prime number")    
