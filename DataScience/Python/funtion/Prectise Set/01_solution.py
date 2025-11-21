i1 = int(input("Enter first number: "))
i2 = int(input("Enter second number: "))
i3 = int(input("Enter third number: "))

l = [i1, i2, i3]
def maximum(l):
    for i in l:
        if i == max(l):
            print(i)

maximum(l)