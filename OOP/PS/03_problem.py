class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} is a dog and it Barks!")

dog = Dog("XYZ")
dog.sound()