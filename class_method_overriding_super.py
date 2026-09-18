class Person:
    def greeting(self):
        print('안녕하세요.')
        
class Student(Person):
    def greeting(self):
        super().greeting() #  Person의 greeting을 호출
        # 중복되는 기능은 파생 클래스에서 다시 만들지 않고, 기반 클래스의 기능을 사용
        print('저는 파이썬 코딩 도장 학생입니다.')
        
james=Student()
james.greeting()

'''
메서드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용
'''
