# 함수 안에서 함수 만들기

def print_hello():
    hello='Hello, Python!'
    def print_message():
        print(hello)
    print_message()
    
print_hello()