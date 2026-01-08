from functools import reduce
l = [2, 5, 6, 55, 6, 8, 98, 9, 23]

def greater(a, b):
    if (a>b):
        return a
    return b
print(reduce(greater, l))