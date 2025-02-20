# Label the program written in problem 4 with comments.


import os  # Import the os module to interact with the operating system

# Define the directory path to list its contents
directory_path = '/'  # Root directory ("/" for Linux/macOS, change as needed)

# Get the list of files and directories in the specified path
contents = os.listdir(directory_path)

# Loop through the contents and print each item
for item in contents:
    print(item)  # Display the file or directory name
