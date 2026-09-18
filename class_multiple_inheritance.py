class Person:
    def greeting(self):
        print('안녕하세요.')
        
class University:
    def manage_credit(self):
        print('학점관리')
        
class Undergraduate(Person,University):
    def study(self):
        print('공부하기')
        
james=Undergraduate()
james.greeting()
james.manage_credit()
james.study()
