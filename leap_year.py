def is_leap_year(year):
    # 윤년인지 평년인지 판단하는 함수
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # 윤년
    else:
        return False  # 평년

# 사용자로부터 연도를 입력받음
year = int(input("연도를 입력하세요: "))

# 판단 결과 출력
if is_leap_year(year):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다.")
