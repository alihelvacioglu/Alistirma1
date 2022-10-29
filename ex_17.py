def number(x):
    if a in range(100,10000):
       print("you are on the interval of the propability for calculating")
    else:
       print("please enter a number with 3 or 4 digits")
    if x== int(str(x)[::-1]):
       print(x,"is a palindromic number")
    else:
       print(x,"is not a palindromic number")           
a=int(input("enter a number with 3 or 4 digits:"))
number(a)       