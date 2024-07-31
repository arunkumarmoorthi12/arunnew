def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
number= int(input("enter a number to calculate its factorial : "))
if number <0:
    print("factorial is not defined for number ",number)
else:
    print("factorial of ",number,"is",factorial(number))
