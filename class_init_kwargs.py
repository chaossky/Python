class Person:
    def __init__(self,**kwargs):
        self.name=kwargs['name']
        self.age=kwargs['age']
        self.address=kwargs['address']
        
maria1=Person(name='마리아',age=20,address='서울시 서초구 반포동')
maria2=Person(**{'name':'마리아','age':20,'address':'서울시 서초구 반포동'})

print(maria1.name)
print(maria1.age)
print(maria1.address)

print(maria2.name)
print(maria2.age)
print(maria2.address)