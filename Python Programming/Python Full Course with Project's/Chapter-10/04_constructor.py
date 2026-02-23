class Employee:
    name = "Geetansh"
    language = "Py"
    salary = 16000000

    def __init__(
        self, name, salary, language
    ):  # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("here is the code")

    def getinfo(self):
        print(
            f"This is the language {self.language}.This is my Salary is {self.salary} "
        )


Geetansh = Employee("Geetansh", 180000000000, "JavaScript")


print(Geetansh.name, Geetansh.language, Geetansh.salary)
