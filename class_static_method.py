class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)
        
    @staticmethod
    def mul(a,b):
        print(a*b)
        
# 클래스에서 바로 메서드 호출        
Calc.add(10,20)
Calc.mul(10,20)

'''
정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없습니다. 
그래서 보통 정적 메서드는 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용합니다.
정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는 
순수 함수(pure function)를 만들 때 사용
순수 함수는 부수 효과(side effect)가 없고 입력 값이 같으면 언제나 같은 출력 값을 반환
정적 메서드는 인스턴스의 상태를 변화시키지 않는 메서드를 만들 때 사용합니다.
'''
