def hello():
    print("Hello")
    
def add_num(a,b): #특별한 자료형을 지정하지 않았다.
    """두개를 더한다. 
    숫자, 문자, 리스트, 튜플, 실수와 정수의 덧셈은 실수로 변환되어 출력
    리스트, 튜플은 두개를 합친 리스트나 튜플이 만들어 진다.
    """
    return a+b #

hello()
print(add_num(1,2))
print(add_num('one','two'))
#print(add_num('one',2))
print(add_num(1.0,2.0))
print(add_num(1.2,2.3))
print(add_num(1.0,2)) 
print(add_num([1,2,3],[4,5,6]))
print(add_num((1,2,3),(4,5,6)))
#print(add_num({1,2,3},{4,5,6}))
#print(add_num({'a':1,'b':2},{'c':3,'d':4})) 

print(add_num.__doc__)
help(add_num)