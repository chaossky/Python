import math

def distance2D(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

d1=distance2D(3,1,5,0)

print(d1)