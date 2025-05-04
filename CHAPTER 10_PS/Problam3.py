class Damo:
    a = 4
    
    
o = Damo()
print(o.a) # Prints the class attribute because instance attribute is not present 

o.a = 0  # Instance attribut is set
print(o.a)  # Prints the class attribute because instance attribute is present

print(Damo.a)  # Prints the class attribute