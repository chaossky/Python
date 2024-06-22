class Base1:
    l=12
    def length(self):
        return self.l
class Base2:
    b=20            
    def breadth(self):
        return self.b
class Derived(Base1,Base2):
    def area(self):
        return self.l*self.b

reg=Derived()
print("Length of the region:",reg.length())
print("Breadth of the region:",reg.breadth())
print("Area of the region:",reg.area())
