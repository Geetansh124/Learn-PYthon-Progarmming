a = int(input("Enter a Number: "))
b = int(input("Enter Second Number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our programmer is not ment to divide number by zero")

else:
    print(f"The  dvision a/b is {a/b}")