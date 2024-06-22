import turtle as t

t.bgcolor('black')

t.speed(0)

for x in range(200):
    if x%3==0:
        cl='red'
    elif x%3==1:
        cl='blue'
    elif x%3==2:
        cl='yellow'

t.color(cl)

t.forward(x*2)

t.left(119)