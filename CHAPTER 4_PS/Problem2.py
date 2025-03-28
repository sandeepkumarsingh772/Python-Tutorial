# Write a program to accept the marks of 6 students and display then in a sorted manner.

marks = []

for i in range(6):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

    marks.sort()

print("\nList of marks:", marks)

