class Animals:
    pass



class pets(Animals):
    @staticmethod
    def bark():
        print("Bow Bow!")



class Dog(pets):
    pass

d = Dog()

d.bark()