class Person:
    def __init__(self):
        self.bag=[]
        
    def put_bag(self,stuff):
        self.bag.append(stuff)
        
james=Person()
james.put_bag('책')

maria=Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag) 

'''
인스턴스 속성은 인스턴스별로 독립되어 있으며 서로 영향을 주지 않습니다.

클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용

인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

'''
