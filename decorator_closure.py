"""
데코레이터는 호출할 함수를 매개변수로 받는다.
호출할 함수를 감싸는 함수 Wrapperfmf aksemsek.
매개변수로 받은 함수의 원래 이름을 출력 할때는 __name__ 속성을 활용.
return 을 사용하여 wrapper 함수 자체를 반환
함수 안에서 함수를 만들고 반환 하는 클로져    
"""

def trace(func):
    def wrapper():
        print(func.__name__,'함수 시작')
        func()
        print(func.__name__,'함수 끝!')
    return wrapper

def hello():
    print('hello')
    
def world():
    print('world')
    
trace_hello=trace(hello)
trace_hello()
trace_world=trace(world)
trace_world()