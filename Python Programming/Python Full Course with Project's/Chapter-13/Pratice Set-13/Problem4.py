def divisiible5(n):
    if(n%5 == 0):
        return True
    return False

a = [2, 5, 6, 55, 6, 8, 98, 9, 23]

f = list(filter(divisiible5, a))

print(f)