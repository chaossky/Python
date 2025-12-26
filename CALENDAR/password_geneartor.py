import random
import string

def generate_password(length=8):
    if length < 6:
        raise ValueError("비밀번호 길이는 최소 6자 이상이어야 합니다.")

    # 필수 요소: 대문자, 소문자, 숫자
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)

    # 나머지 문자들 (대문자 + 소문자 + 숫자)
    all_chars = string.ascii_letters + string.digits

    # 나머지 길이만큼 랜덤 선택
    remaining = [random.choice(all_chars) for _ in range(length - 3)]

    # 전체 조합
    password_list = [upper, lower, digit] + remaining

    # 순서 섞기
    random.shuffle(password_list)

    return ''.join(password_list)

# 여기서 실제로 함수를 호출해야 결과가 나옵니다!
print(generate_password(8))   # 8자리 비밀번호 출력
print(generate_password(12))  # 12자리 비밀번호 출력
