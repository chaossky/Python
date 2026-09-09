class Person:
    def __init__(self,name, age, address):# 인스턴스를 만들때 호출되는 특별한 메서드
        self.hello='안녕하세요.'
        self.name=name
        self.age=age
        self.address=address
        #self는 인스턴스 자신을 의미
    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello,self.name))
        
maria=Person('마리아',20,'서울시 서초구 반포동')
maria.greeting()

print('이름 : ',maria.name)
print('나이 : ',maria.age)
print('주소 : ',maria.address)
'''
클래스 안에서 속성에 접근할 때는 self.속성 형식이었죠? 
클래스 바깥에서 속성에 접근할 때는 인스턴스.속성 형식으로 접근
'''
# 인스턴스를 통해 접근하는 속성 인스턴스 속성
