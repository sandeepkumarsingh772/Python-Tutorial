a = int(input("Enter the age: "))

# if statmenet no: 1
if (a%2 == 0):
    print("a is evane")
# End of if statement no: 1

# if statement no: 2
if (a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif (a<=0):
    print("You are entering an invalid negative age ")
else:
    print("You are below the age of consent")
# End of if statement no:2

print("End of program")