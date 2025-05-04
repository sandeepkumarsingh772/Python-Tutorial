class Employee:
    language = "Python"  # This is a class attribute 
    salary = 1200000
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
        
    def geet(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    
sandeep = Employee()
sandeep.language = "JavaScript"  # This is an instance attribute


sandeep.geet()
sandeep.getinfo()
Employee.geet(sandeep)