# A spam comment is defiend as a text containing follwoing keywoads:

p1 = "Make a lot of monye"
p2 = "boy Now"
p3 = "subscribe this"
p4 = "clicke this"

message = input("Enter your comment:  ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")
else:
    print("This comment is not a spam")