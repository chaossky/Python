from PIL import Image, ImageDraw, ImageFont

# 이미지 설정
img_width, img_height = 800, 400
img = Image.new('RGB', (img_width, img_height), color="lightblueg")
draw = ImageDraw.Draw(img)

# 한글 지원 폰트 경로 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 또는 다운로드한 나눔글꼴 경로
font = ImageFont.truetype(font_path, size=60)

# 텍스트 설정
text = "긍정적인 하루 되세요!"

# 텍스트 크기 계산
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# 가운데 위치 계산
x = (img_width - text_width) / 2
y = (img_height - text_height) / 2

# 텍스트 그리기
draw.text((x, y), text, font=font, fill=(0, 0, 0))

# 이미지 저장
img.save("positive_quote_centered.png")
