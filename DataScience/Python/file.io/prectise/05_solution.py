def replace():
    word = ["Varun", "Washington", "Nitish"]
    with open("list.txt", "r") as f:
        content = f.read()
        with open("list.txt", "w") as f:
            for w in word:
                content = content.replace(w, "#####")
            return f.write(content)
replace()