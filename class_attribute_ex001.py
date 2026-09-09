class Person:
    bag=[]
    
    def put_bag(self,stuff):
        self.bag.append(stuff)
        
james=Person()
james.put_bag('책')

maria=Person()
maria.put_bag('열쇠')

# james와 maria 인스턴스를 만들었다.
# 그런데, 같은 클래스 이게 때문에, 모든 인스턴스에서 클래스 속성을 공유한다.
print(james.bag)
print(maria.bag)

print(james.__dict__)
print(maria.__dict__)

print(Person.__dict__)