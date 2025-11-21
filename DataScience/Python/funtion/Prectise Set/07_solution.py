l = ["Harry", "Sohan", "Sachin", "Rahul"]

def rm(l, word):
    n = []
    for i in l:
        if not(i == word):
            n.append((i.strip(word)))
        return n
    
l = ["Harry", "Sohan", "Sachin", "Rahul"]

print(rm(l, "Sachin"))