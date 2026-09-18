class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕하세요.' #  기반 클래스 Person의 __init__ 메서드를 호출해주면 기반 클래스가 초기화되어서 속성이 만들어집니다.
        
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school='코딩도장'
        
james=Student()
print(james.school)
print(james.hello)