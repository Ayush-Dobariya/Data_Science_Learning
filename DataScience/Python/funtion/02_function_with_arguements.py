def f(n):
    if(n == 1 or n == 0):
        return 1
    return n * f(n-1)

n = int(input("Enter a number to find its factorial: "))
result = f(n)
                              
print(result)