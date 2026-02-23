def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)


pattern(3)    
pattern(int(input("Enter the numbers of rows:")))