# write a program to find out whether a student has passed or failed if it requries a totalof 40% 
# and least 33% in each subject to pass.Assume 3 subject and take marks as an input from the user.

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if (total_percentage>=40 and marks1>=30 and marks2>=30 and marks3>=30):
    print("You are passed:", total_percentage)
else:
    print("you failed, try again next year:", total_percentage)