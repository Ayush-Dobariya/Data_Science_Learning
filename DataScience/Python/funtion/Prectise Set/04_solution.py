n = 4

def recultion(n):
    if n == 1:
        return 1
    return recultion(n - 1) + n
print(recultion(n))