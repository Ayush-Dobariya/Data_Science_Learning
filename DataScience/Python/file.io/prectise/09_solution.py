with open("file1.txt", "r") as file1:
    content = file1.read()
with open("file2.txt", "r") as file2:
    content2 = file2.read()
if content == content2:
    print("The contents of both files are identical.")