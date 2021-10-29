def factorial(n):
    if n < 1:
        return 1
    else:
        returnNumber = n * factorial(n-1)
        print(n,"! = ", returnNumber)
        return returnNumber
