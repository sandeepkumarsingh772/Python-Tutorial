class Employee:
    language = "python" # This is a class attribute 
    salary = 1200000
    

sandeep = Employee()
sandeep.language = "JavaScript"    # This is an instance attribute
print(sandeep.language, sandeep.salary)

