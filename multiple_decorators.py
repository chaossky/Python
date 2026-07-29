def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')
    
hello()