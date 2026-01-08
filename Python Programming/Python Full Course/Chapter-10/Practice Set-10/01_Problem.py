class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin    


p = Programmer("Geetansh", 18000000, 2006)

print(p.name, p.salary, p.pin)

d = Programmer("Django", 18000000, 2006)

print(d.name, d.salary, d.pin)


