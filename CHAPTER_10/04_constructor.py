class Employee:
    language = "Python"  # This is a class attribute 
    salary = 1200000
    
    
    def __init__(self, language, salary):      # Dunder method which is automaticall called
        
        self.language = language
        self.salary = salary
        print("I am creating an object ")
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
        
    def geet(self):
        print("Good Morning")

    
sandeep = Employee("Python", 1300000)
sandeep.language = "JavaScript"  # This is an instance attribute
print(sandeep.language, sandeep.salary)


sandeep.geet()
sandeep.getinfo()
# Employee.geet(sandeep)