from collections import defaultdict

# 주어진 집값 데이터
data = [56, 89, 165, 73, 83, 145, 90, 189, 127, 77, 110, 112, 132,
        120, 94, 130, 84, 65, 99, 154, 86, 120, 122, 103, 130]

# 줄기-잎 구조 생성
stem_leaf = defaultdict(list)
for number in data:
    stem = number // 10   # 십의 자리
    leaf = number % 10    # 일의 자리
    stem_leaf[stem].append(leaf)

# 출력: 줄기 오름차순, 잎 오름차순
print("줄기 | 잎")
print("------------")
for stem in sorted(stem_leaf.keys()):
    leaves = sorted(stem_leaf[stem])
    leaf_str = ' '.join(str(leaf) for leaf in leaves)
    print(f"{stem:>4} | {leaf_str}")
