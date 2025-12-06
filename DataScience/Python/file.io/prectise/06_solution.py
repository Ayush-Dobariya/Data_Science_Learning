def find():
    with open("log.txt", "r") as f:
        content = f.read()
        lines = f.readlines()
        lineno = 1
        for line in lines:
            if("python" in line):
                print(f"Line Number is : {line}")
                lineno += 1
                break
            else:
                print("Python is not found in the file.")
           
     
        

find()