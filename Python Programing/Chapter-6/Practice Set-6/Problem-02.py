marks1 = int(input("Enter Marks for Sbject 1: "))
marks2 = int(input("Enter Marks for Sbject 2: "))
marks3 = int(input("Enter Marks for Sbject 3: "))

# Check for Total Percentage    

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40):
    print("You are Passed")

else:
    print("You Failed")    