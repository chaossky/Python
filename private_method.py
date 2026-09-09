class Person:
    def __greeting(self):
        print('Hello')
        
    def hello(self):
        self.__greeting()
        
james=Person()
#james.__greeting()
james.hello()

            