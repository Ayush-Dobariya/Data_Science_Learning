obj = {
    "90-100":"Exellent",
    "80-90": "A",
    "70-80": "B",
    "60-70": "C",
    "50-60": "D",
    "50-0": "Fail"
}

Marks = int(input("Enter You marks:"))

if(Marks >= 90):
    print(f"Your performance is {obj['90-100']}")
elif(Marks >= 80 and Marks <=90 ):
    print(f"Your performance is {obj['80-90']}")
elif(Marks >= 70 and Marks <=80 ):
    print(f"Your performance is {obj['70-80']}")
elif(Marks >= 60 and Marks <=70 ):
    print(f"Your performance is {obj['60-70']}")
elif(Marks >= 50 and Marks <=60 ):
    print(f"Your performance is {obj['50-60']}")
elif(Marks >= 0 and Marks <=50 ):
    print("You're faild")