def A():
    x=10 # A의 지역변수 x
    def B():
        nonlocal x 
        x=20 # 현재 함수의 바깥쪽에 있는 지역변수 사용 A의 지역 변수 x에 20할당
        
    B()
    print(x) # A의 지역변수 x 출력
    
A()