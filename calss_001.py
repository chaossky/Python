"""
객체
클래스로 표현
클래스 안에는 속성과 메소드가 존재
객체지향 프로그래밍
복잡한 문제를 추상화 객체화
객체를 조합해서 문제해결
파이썬에서는 모든 것이 객체
보통 클래스 이름은 대문자로 시작
메서드는 함수
반드시 들여쓰기

"""
class Person:
    def __init__(self):
        self.hello='안녕하세요.'
        
    def greeting(self):
        print(self.hello)
        

        
james=Person()

james.greeting()      
        
        