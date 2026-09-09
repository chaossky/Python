class Person:
    def __init__(self,name,age,address,wallet):
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
        
    def pay(self,amount):
        if amount>self.__wallet:
            print('돈이 모자랍니다.')
            return
        self.__wallet -=amount
        print('이제 {0}원 남았습니다.'.format(self.__wallet))
        
maria=Person('마리아',20,'서울시 서초구 반포동',10000)
maria.pay(3000)

print(maria.name)
print(maria.age)
print(maria.address)
# print(maria.__wallet)
