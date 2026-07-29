import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.width(2)

h=0

for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,1)
    h +=0.005
    t.color(c)
    t.circle(150)
    t.left(1)
        
turtle.done()