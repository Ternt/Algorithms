def fibonacci(n):
    if n == 0 or n == 1: #base case
        return n
    return fibonacci(n-2)+fibonacci(n-1) #recursive case


for n in range(15):
    print(fibonacci(n))
