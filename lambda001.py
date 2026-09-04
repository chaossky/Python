"""
    람다 표현식 
        람다 표현식을 배워 본다.
"""

# from functools import reduce

# square=lambda x:x**2

# print(square(4))
# print(square(10))

# add=lambda x,y:x+y
# result=add(2,3)
# print(result)

# # 조건문 활용
# is_even=lambda x:True if x%2==0 else False
# print(is_even(22))
# print(is_even(23))

# #for문 활용
# numbers=[1,2,3,4,5]
# double_numbers=[(lambda x:x*2)(x) for x in numbers]
# print(double_numbers)

# #map 함수 사용
# squared=list(map(lambda x:x**2,numbers))
# print(squared)

# #filter 함수 사용
# numbers2=[1,2,3,4,5,6,7,8,9,10]
# even_num=list(filter(lambda x:x%2==0,numbers2))
# print(even_num)

# #reduce 함수
# sum01=reduce(lambda x,y:x+y,[0,1,2,3,4])
# print(sum01)


#print(reduce(lambda x,y:y+x,'abcde'))

# data = [
#     (11, 'lemon'),
#     (3, 'banana'),
#     (20, 'watermelon'),
#     (1, 'apple'),
#     (16, 'strawberry'),
#     (7, 'fig'),
#     (18, 'ugli fruit'),
#     (14, 'quince'),
#     (5, 'date'),
#     (9, 'honeydew'),
#     (2, 'cherry'),
#     (12, 'orange'),
#     (6, 'grape'),
#     (19, 'tangerine'),
#     (4, 'elderberry'),
#     (15, 'papaya'),
#     (8, 'kiwi'),
#     (10, 'mango'),
#     (17, 'raspberry'),
#     (13, 'nectarine')
# ]

# # 두 번째 요소(과일 이름) 기준으로 정렬
# sorted_data = sorted(data, key=lambda x: x[0])
# print(sorted_data)

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95},
    {"name": "Ethan", "score": 88}
]

# # 점수 높은 순으로 정렬

# print("높은 점수 순으로 정렬")
# sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
# print(sorted_students)

# print("80점 이상인 학생만 뽑기")
# high_scorers = list(filter(lambda x: x["score"] >= 80, students))
# print(high_scorers)

# print("학생 이름만 뽑아서 대문자로 변환하는 경우")
# names_upper = list(map(lambda x: x["name"].upper(), students))
# print(names_upper)

# print("점수에 따라 등급을 나누는 복잡한 조건을 람다로 작성")
# print("가독성이 떨어질수 있음")
# grade = list(map(lambda x: "A" if x["score"] >= 90 else ("B" if x["score"] >= 80 else "C"), students))
# print(grade)

# def get_grade(student):
#     if student["score"] >= 90:
#         return "A"
#     elif student["score"] >= 80:
#         return "B"
#     else:
#         return "C"

# grade = list(map(get_grade, students))
# print(grade)

# 80점 이상인 학생만 필터링
high_scorers = filter(lambda x: x["score"] >= 80, students)

# 등급 계산: A=90 이상, B=80~89, C=그 외
for student in high_scorers:
    grade = (lambda s: "A" if s >= 90 else "B" if s >= 80 else "C")(student["score"])
    print(student["name"], grade)