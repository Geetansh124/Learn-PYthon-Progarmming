a = int(input("Enter Your Age :"))

# If elif else ladder
if(a>=18):
    print("Your are above the age of consent")
    print("Good for You ")

elif(a<0):
    print("You are Entering invelid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")        

else:
    print("Your are below the age of consent")


print("Try entering Right age")        