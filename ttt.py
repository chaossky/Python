class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Sayhello(self):
        print ('Hello my name is',self.name)
        
    def __del__(self):
        print("%s says bye." % self.name)
        
        
A=Person("Lee Janghoon",25)
A.Sayhello()
del A

