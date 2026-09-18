class Person:
    def greeting(self):
        print('안녕하세요.')
        
class PersonList:
    def __init__(self):
        self.person_list=[]
        
    def append_person(self,person):
        self.person_list.append(person)