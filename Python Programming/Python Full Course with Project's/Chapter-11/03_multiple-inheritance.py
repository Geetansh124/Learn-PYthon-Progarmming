class Employee:
    a = 1

class Programmer(Employee):
    b = 2    


class Manager(Programmer):
    c = 3




o = Employee()
print(o.a) # Print the attribut
# print(o.b) # Shows an error as there is no b attribut in Employee class

o = Programmer()
print(o.a, o.b)
     
     
o = Manager()
print(o.a, o.b, o.c)

