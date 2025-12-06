def replace():
    word = input("Enter the word to be replaced: ")
    with open("que4.txt", "r") as f:
        content = f.read()
        with open("que4.txt", "w") as f:
            content = content.replace(word, "#####")
            return f.write(content)
replace()