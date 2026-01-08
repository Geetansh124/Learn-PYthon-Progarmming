class Employee:
    def __init__(self):
        print("Constrctor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constrctor of Programmer")
    b = 2    


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constrctor of Manager")
    c = 3




# o = Employee()
# print(o.a) # Print the attribut
# print(o.b) # Shows an error as there is no b attribut in Employee class

# o = Programmer()
# print(o.a, o.b)
     
     
o = Manager()
print(o.a, o.b, o.c)

