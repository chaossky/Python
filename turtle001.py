import turtle
import colorsys

screen=turtle.Screen()
screen.bgcolor("black")
screen.colormode(1.0)

t=turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

n=36
h=0

for i in range(460):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h +=1/n
    t.color(c)
    t.left(145)
    
    for j in range(5):
        t.forward(300)
        t.left(150)
        
turtle.done()