marks1 = int(input("Enter Marks for Sbject 1: "))
marks2 = int(input("Enter Marks for Sbject 2: "))
marks3 = int(input("Enter Marks for Sbject 3: "))

# Check for Total Percentage    

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Passed", total_percentage)

else:
    print("You Failed", total_percentage)    