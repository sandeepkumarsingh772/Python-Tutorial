# write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + 1

print(sum(4))