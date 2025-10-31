# Strings and Character Data in Python - Practice Examples

# 1. 문자열 리터럴과 이스케이프
a = 'hello'
b = "hello"
c = '''여러 줄
문자열'''
d = r"\n은 줄바꿈이 아님"
e = "스마일: \U0001F600"
f = "이름: \N{GREEK SMALL LETTER PI}"

print(a, b, c, d, e, f, sep=" | ")

# 2. 인덱싱과 슬라이싱
s = "Python🐍"
print(s[0], s[-1], s[1:4], s[::-1])

# 3. 문자열은 불변
s = "cat"
# s[0] = 'b'  # 불가능
s = "b" + s[1:]
print("수정된 문자열:", s)

# 4. 문자열 메서드
t = "  Hello, World!  "
print(t.strip())
print("spam,eggs,ham".split(","))
print("line1\nline2".splitlines())
print(",".join(["a", "b", "c"]))
print("hello".replace("l", "L", 1))
print("abc".isalpha(), "123".isdigit(), "Ⅳ".isnumeric())
print("straße".casefold())

# 5. 문자열 포매팅
name = "Lee"
score = 93.456
print(f"{name}: {score:.1f}")
x = 42
print(f"{x=}")
from datetime import date
today = date(2025, 8, 23)
print(f"{today:%Y-%m-%d}")

print("{name}: {score:.2f}".format(name="Lee", score=93.456))
print("%s: %.2f" % ("Lee", 93.456))

from string import Template
print(Template("$who scored $what").substitute(who="Lee", what=95))

# 6. 유니코드 정규화
import unicodedata as ud
s1 = "é"        # U+00E9
s2 = "e\u0301"  # 'e' + 결합악센트
print("동일 여부:", s1 == s2)
print("정규화 후:", ud.normalize("NFC", s2) == s1)

# 7. str vs bytes
text = "파이썬🐍"
data = text.encode("utf-8")
print("문자열 길이:", len(text), "바이트 길이:", len(data))
back = data.decode("utf-8")
print("복원:", back)

# 8. 정규표현식
import re
pat = re.compile(r"\b\w+\b")
print(re.findall(pat, "Hello, world!"))
print(re.sub(r"\s+", " ", "a  b   c"))

# 9. 성능 팁 - join
parts = []
for i in range(5):
    parts.append(str(i))
result = "-".join(parts)
print(result)

# 10. 작은 치트시트
s = "banana"
print(s.startswith("ba"), s.endswith("na"))
print("  x  ".strip())
print(f"{'x':^5}")
print("banana".replace("na", "NA", 1))
print("Straße".casefold() == "STRASSE".casefold())
