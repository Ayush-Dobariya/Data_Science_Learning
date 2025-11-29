st = "This is the 29th november its really nostalgic!"

f = open("f12.txt", "w")

text = f.write(st)
print(text) # this will print number of charcters of file
f.close()