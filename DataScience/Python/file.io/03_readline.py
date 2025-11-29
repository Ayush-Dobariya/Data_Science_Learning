f = open("hello.txt")

lines = f.readlines()

print(lines, type(lines))

f.close()