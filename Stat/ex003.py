# 학생들의 선호 운동 데이터
sports_data = {
    "농구": 10,
    "야구": 7,
    "미식축구": 6,
    "축구": 5,
    "테니스": 5,
    "하키": 2
}

# 전체 학생 수
total_students = sum(sports_data.values())

# 도수·상대 도수 분포표 출력
print("도수·상대 도수 분포표")
print("{:<10} {:<5} {:<10}".format("운동", "도수", "상대도수(%)"))
print("-" * 30)

for sport, count in sports_data.items():
    relative_freq = (count / total_students) * 100
    print("{:<10} {:<5} {:<10.2f}".format(sport, count, relative_freq))

# 합계 확인
print("-" * 30)
print("{:<10} {:<5} {:<10}".format("합계", total_students, "100.00"))
