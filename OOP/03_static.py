class Employee:
    name = "Ayush"
    Langueges = "Python"
    salary = 10000000000000
    def getInfo(self):
        print(f"The languege is {self.Langueges} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning, Sir!")
harry = Employee()
harry.getInfo()
harry.greet()
