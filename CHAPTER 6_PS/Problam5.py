# Write a program which finds out whether a given name is present in a last or not.

l = [ "Sandeep", "Harry", "Rohan", "Shubham", "Divya"]

name = input("Enter your name: ")

if (name in l):
    print("Your name in the list")
else:
    print("Your name is not in the list")