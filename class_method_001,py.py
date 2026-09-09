class Person:
    count=0 #클래스 속성
    
    def __init__(self):
        Person.count +=1
        
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))
    @classmethod
    def create(cls):
        p=cls()
        return p
        
james=Person()
maria=Person()
john=Person()

Person.print_count()