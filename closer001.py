x=10 # 전역 변수

def foo():
    global x # 전역 변수 x를 사용하겠다고 설정
    x=20 # 전역변수 x
    print(x) # 전역 변수를 출력
    
foo()
print(x) # 전역 변수 출력
# x는 각각 이름은 같지만, 서로 다른 변수.

# 현재의 네임스페이스를 딕셔너리 형태로 출력할 수 있다.
print(locals())