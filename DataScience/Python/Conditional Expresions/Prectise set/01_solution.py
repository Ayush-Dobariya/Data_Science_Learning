i1 = int(input("Enter nummber:"))
i2 = int(input("Enter nummber:"))
i3 = int(input("Enter nummber:"))
i4 = int(input("Enter nummber:"))

if(i1>i2 and i1>i3 and i1>i4):
    print(i1,"is the greatest number")
elif(i2>i1 and i2>i3 and i2>i4):
    print(i2,"is the greatest number")  
elif(i3>i1 and i3>i2 and i3>i4):
    print(i3,"is the greatest number")
else:
    print(i4,"is the greatest number")