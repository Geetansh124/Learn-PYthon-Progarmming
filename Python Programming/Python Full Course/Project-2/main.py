import random
n = random.randint(1, 100)
a = -1
guesses = 
while(a != n):
    a = int(input("Guess the number:"))
    if(a>n):
        print("Lower Number please")
        guesses +=1
    elif(a<n):
        print("Higher Number please")
        guesses +=1

print(f"You have gusses the number {n} correctly in {guesses} attempt")




