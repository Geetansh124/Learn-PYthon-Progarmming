'''
1 for snake 
-1 for water
0 for gun
'''
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]

# By now we have 2 variables, computer and you with values (-1,0,1)

print(f"Your Choice {reverseDict[you]}\nComputer Choice {reverseDict[computer]}")

if(computer == you):
     print("Its a Draw!")

     
else:
    if(computer ==-1 and you ==1):
        print("You Win!")

    elif(computer ==-1 and you ==0):
        print("You Lose!")


    elif(computer ==1 and you ==-1):
        print("You Lose!")

    elif(computer ==-1 and you ==0):
        print("You Win!")   

    elif(computer ==0 and you ==-1):
        print("You Lose!")

    elif(computer ==0 and you ==1):
        print("You Win!")    

    else:
        print("Something went wrong!")    

# else:
#     if((computer - you) == -1 or(computer - you) == 2):
#         print("You Lose!")
        
#     else:
#         print("You Win!")    