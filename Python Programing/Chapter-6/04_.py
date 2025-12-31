a = int(input("Enter Your Age :"))

# If statement no. : 1

if(a%2 == 0):
    print("a is even")

# End If statement no: 1

# If statement no. : 2
if(a>=18):
    print("Your are above the age of consent")
    print("Good for You ")

elif(a<0):
    print("You are Entering invelid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")        

else:
    print("Your are below the age of consent")

print("Try to enter right age")    

print("End of Program")