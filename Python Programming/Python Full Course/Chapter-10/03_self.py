class Employee:
    name = "Geetansh"
    language = "Py"
    salary = 16000000
    
    def getinfo(self):
        print(f"This is the language {self.language}.This is my Salary is {self.salary} ")
    
    @staticmethod
    def greet(self):
        print("Good Morning")

Geetansh = Employee()
Geetansh.name = "This is the Class" # This is a instence attribute

print(Geetansh.name, Geetansh.language)
Geetansh.greet()
Geetansh.getinfo()


