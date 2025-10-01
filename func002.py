def add_sub(a,b):
    """두개의 더한 값과 차를 튜플로 반환"""
    return a+b,a-b

print(add_sub(1,2))
print(type(add_sub(1,2)))
x=add_sub(3,5)
a,b=add_sub(10,9)
print(a,b)
print(x)
print(x[0])
print(x[1])
print(x[0],x[1])

print(type(x))