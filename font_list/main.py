import os

# 폰트 폴더 경로
font_dir = "C:\\Windows\\Fonts"

# .ttf 또는 .otf 확장자만 필터링
fonts = [f for f in os.listdir(font_dir) if f.endswith(".ttf") or f.endswith(".otf")]

# 파일로 저장
with open("font_list.txt", "w", encoding="utf-8") as file:
    for font in fonts:
        file.write(font + "\n")

print(f"{len(fonts)}개의 폰트가 font_list.txt에 저장되었습니다.")
