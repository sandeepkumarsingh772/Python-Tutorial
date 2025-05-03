# f = open("/home/admin1/Sandeep/Python-Tutorial/CHAPTER_9/file.txt")

# print(f.read())
# f.close()

with open("/home/admin1/Sandeep/Python-Tutorial/CHAPTER_9/file.txt") as f:
    print(f.read())