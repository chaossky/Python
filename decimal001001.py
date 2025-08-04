import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
rx = x2 - x1
ry = y2 - y1
radian = math.atan2(ry, rx)
degree = radian * 180 / math.pi
round(degree,2)
print(degree)