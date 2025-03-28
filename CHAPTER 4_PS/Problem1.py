#Write a program to store seven fruits in a list entered by the user.


# fruits = []

# for i in range(7):
#     fruit = input("Enter a fruit: ")
#     fruits.append(fruit)

# print(fruits)


# Initialize an empty list to store fruits
fruits = []

# Loop to take 7 fruit names as input
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

# Display the list of fruits
print("\nList of fruits:", fruits)


