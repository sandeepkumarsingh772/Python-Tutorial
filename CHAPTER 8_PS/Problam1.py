# Write a program using function to find greatest of three Numbers.

def greatest(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
    
a = 2
b = 4
c = 5

print(greatest(a, b, c))