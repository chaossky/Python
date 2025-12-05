# 데이터 입력
data = [56, 89, 165, 73, 83, 145, 90, 189, 127, 77, 110, 112, 132,
        120, 94, 130, 84, 65, 99, 154, 86, 120, 122, 103, 130]

# 구간 정의
intervals = {
    "50~74": [],
    "75~99": [],
    "100~124": [],
    "125~149": [],
    "150~174": [],
    "175~200": []
}

# 데이터 분류
for num in data:
    if 50 <= num <= 74:
        intervals["50~74"].append(num)
    elif 75 <= num <= 99:
        intervals["75~99"].append(num)
    elif 100 <= num <= 124:
        intervals["100~124"].append(num)
    elif 125 <= num <= 149:
        intervals["125~149"].append(num)
    elif 150 <= num <= 174:
        intervals["150~174"].append(num)
    elif 175 <= num <= 200:
        intervals["175~200"].append(num)

# 출력
print("   줄기   |      잎")
for stem, leaves in intervals.items():
    if leaves:  # 값이 있는 구간만 출력
        leaves_sorted = sorted(leaves)
        # 각 값은 두 자리로 맞추기 (예: 03, 10)
        leaf_str = " ".join(f"{x%100:02d}" for x in leaves_sorted)
        print(f"{stem:<9} |  {leaf_str}")
