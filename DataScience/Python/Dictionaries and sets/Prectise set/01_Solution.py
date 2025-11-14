dict = {
    "Aloo": "Potato",
    "Bhindi": "Okra",
    "Ghadi": "Watch"
}

print("Welcome to the Hindi to English Dictionary!")
word = input("Enter a Hindi word to translate: ")

trans = dict.get(word)
print(f"The Translation is : {trans}")