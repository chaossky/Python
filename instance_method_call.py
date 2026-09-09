class Person:
    def greeting(self):
        self.hello='안녕하세요'
        
maria=Person()
# 인스턴스는 생성한뒤 속성을 추가할 수 있다.
# __init__ 메서드가 아닌 다른 메서드에서도 속성을 추가할 수 있다.
# 이때 메서드를 호출해야 속성이 생긴다.
maria.greeting() #greeting 메서를 호출하면 hello 속성이 생성
print(maria.hello)

'''
    인스턴스는 자유롭게 속성을 추가할 수 있따.
    특정 속성만 허용하고 다른 속성은 제한하고 싶다면,
    클래스에서 __slots__에 허용할 속성 이름을 리스트에 넣어 주어야 한다.
    속성이름은 반드시 문자열로 지정해 준다.
'''
