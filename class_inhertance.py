class Person:
    def greeting(self):
        print('안뇽')
        
class Student(Person):
    def study(self):
        print('공부하기')
        
james=Student()
james.greeting()
james.study()

if issubclass(Student,Person):
    print('하부 클래스 맞아요.')
else:
    print('하부 클래스 아니에요.')
    