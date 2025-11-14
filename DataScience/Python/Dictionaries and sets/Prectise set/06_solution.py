dict = {
    "F1": "",
    "F2": "",
    "F3":"",
    "F4":""
}

# f1 = dict[0] = input("Name of first friend:")
# f2 = dict[1] = input("Name of second friend:")
# f3 = dict[2] = input("Name of third friend:")
# f4 = dict[3] = input("Name of fourth friend:")

# print(dict.keys())

dict.update({"F1": input("Name of first friend:"),})
dict.update({"F2": input("Name of second friend:"),})
dict.update({"F3": input("Name of third friend:"),})
dict.update({"F4": input("Name of fourth friend:"),})


print(dict)