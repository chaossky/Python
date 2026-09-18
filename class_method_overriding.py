class Person:
    def greeting(self):
        print('안녕하세요')
        
class Student(Person):
    def greeting(self):
        print('안녕하세요. 파이썬 코딩 도장입니다.')
        
james=Student()
james.greeting()