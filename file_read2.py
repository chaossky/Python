with open('hi_oo.txt','r') as file:
    s=file.read()
    print(s)
    
    # with ~~~ as 를 사용하면 파일 객체를 자동으로 닫아 준다.
    