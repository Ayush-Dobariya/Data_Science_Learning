# '''
#   *
#  ***
# *****
# '''

# n = int(input("Enter the number of rows: "))

# for i in range(1, n+1):
#     print(" "*(n-i))
#     print(("*")*(2*i-1) , end="")
#     print(" ")


# n = int(input("Enter the number of rows: "))

# for i in range(1, n+1):
#     print(" "*(n-i))
#     print(("*")*(i) , end="")
#     print(" ")

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    if i ==1 or i ==n:
      print("*"*n)
    else:
         print("*", end ="")
         print(" "*(n-2), end ="")
         print("*", end="")
    print("")