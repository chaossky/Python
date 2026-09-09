class Person():
    ''' 사람 클래스 입니다. '''
    
    def greeting(self):
        ''' 인사 메서드 입니다. '''
        print('Hello')
        
print(Person.__doc__)
print(Person.greeting.__doc__)

maria=Person()
print(maria.greeting.__doc__)