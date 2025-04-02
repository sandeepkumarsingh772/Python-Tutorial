# Write a program to find out whether a given post is taking about "Harry" or Not


post = input("Enter the post: ")

if ("Harry".lower() in post.lower()):
    print("This post taking about harry ")
else:
    print("This post is not taking about harry")

