from PIL import Image, ImageDraw, ImageFont
import os
import platform

# 🔧 줄바꿈 처리 함수
def format_quote(text):
    text = text.strip()
    if "," in text:
        parts = text.split(",", 1)
        return parts[0].strip() + "\n" + parts[1].strip()
    elif len(text) >= 12:
        return text[:12].strip() + "\n" + text[12:].strip()
    else:
        return text

# 📁 이미지 저장 폴더 생성
output_dir = "quotes_images"
os.makedirs(output_dir, exist_ok=True)

# 🎨 이미지 설정
img_width, img_height = 800, 400
bg_color = "lightblue"
text_color = (0, 0, 0)

# 🔠 폰트 설정
font_path = "C:/Windows/Fonts/MalangmalangB.ttf"
font = ImageFont.truetype(font_path, size=60)

# 📜 인용문 텍스트 파일 읽기
with open("quotes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 🖼️ 이미지 생성 루프
for line in lines:
    if "." in line:
        number, quote = line.split(".", 1)
        number = number.strip()
        quote = format_quote(quote)

        # 이미지 생성
        img = Image.new('RGB', (img_width, img_height), color=bg_color)
        draw = ImageDraw.Draw(img)

        # 텍스트 크기 계산
        bbox = draw.textbbox((0, 0), quote, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # 가운데 정렬
        x = (img_width - text_width) / 2
        y = (img_height - text_height) / 2

        # 텍스트 그리기
        draw.text((x, y), quote, font=font, fill=text_color)

        # 파일 저장
        filename = f"quote_{int(number):03}.png"
        filepath = os.path.join(output_dir, filename)
        img.save(filepath)

print(f"{len(lines)}개의 인용문 이미지가 '{output_dir}' 폴더에 저장되었습니다.")
