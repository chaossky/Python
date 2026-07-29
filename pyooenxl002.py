from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "매출데이터"

# 헤더 작성
ws.append(["상품명", "수량", "단가", "합계"])

# 여러 데이터 추가
data = [
    ["사과", 10, 500, "=B2*C2"],
    ["바나나", 5, 300, "=B3*C3"],
    ["포도", 8, 700, "=B4*C4"],
    ["딸기", 12, 1000, "=B5*C5"],
    ["오렌지", 15, 400, "=B6*C6"],
    ["복숭아", 7, 800, "=B7*C7"],
    ["키위", 20, 350, "=B8*C8"],
    ["망고", 9, 1200, "=B9*C9"],
    ["수박", 3, 5000, "=B10*C10"],
    ["메론", 4, 4500, "=B11*C11"]
]

for row in data:
    ws.append(row)

wb.save("sales.xlsx")
