class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕하세요.'
        
class Student(Person):
    pass

james=Student()
print(james.hello)

'''
파생 클래스에서 __init__ 메서드를 생략한다면 
기반 클래스의 __init__이 자동으로 호출
super()는 사용하지 않아도 됩니다.
'''
