# Write a program to fill in a letter template given below with name and date.
letter = '''
            Dear <|name|>,
            You are selected!
            Date: <|Date|>
                   ''' 

print(letter.replace("<|name|>", "Sandeep").replace("<|Date|>", "25-03-2025"))


# letter = """Dear <|name|>,

# You are selected!
# Date: <|Date|>"""

# print(letter.replace("<|name|>", "Sandeep").replace("<|Date|>", "25-03-2025"))
