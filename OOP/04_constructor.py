class Employee:
    name = "Ayush"
    Langueges = "Python"
    salary = 10000000000000

    def __init__(self, name, salary, lang): # dunder method --> special method and it is called automatically when an object is created
        
        self.name = name
        self.salary = salary
        self.Langueges = lang
        print("Employee is created")


    def getInfo(self):
        print(f"The languege is {self.Langueges} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, Sir!")


harry = Employee("harry", 100000, ["Python", "C++"])
print(harry.name, harry.salary, harry.Langueges)

harry.getInfo()
