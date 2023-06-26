class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def saludo (self) :
     print (f'hola mi nombre es {self.name} y mi edad es {self.age}')
      
p1 = person ("viniza", 19)
p2 = person ("joaquin", 15)
    
print (p1.name)
print (p1.age)
print (p2.name)
print (p2.age)

p1.saludo() 
    