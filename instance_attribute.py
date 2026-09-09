# 클래스로 인스턴스를 만든 뒤에도 인스턴스.속성=값으로 속성을 추가 할 수 있다.

class Person:
    pass

maria=Person()
maria.name='마리아'
print(maria.name)

'''
단 이런 식으로 추가한 속성은 해당 인스턴스에만 생성
클래스로 다른 인스턴스를 만들었을때에는 추가한 속성이 생성되지 않느다.
'''

james=Person()
james.name
