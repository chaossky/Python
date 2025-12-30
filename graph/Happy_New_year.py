import turtle, random
t=turtle.Turtle();t.speed(0)

turtle.bgcolor("#1a1a2e")
t.penup();t.goto(0,-120);t.setheading(140);
t.pendown()

t.color("#ff4d6d","#ff8fa3");t.begin_fill()
t.forward(180);t.circle(-90,200);t.left(120)
t.circle(-90,200);t.forward(180);t.end_fill()
t.penup();t.goto(0,-10);t.color("white")

t.write("Happy New Year 2026",align="center",font=("Arial",22,"bold"))
t.color("yellow")

for _ in range(300):
    t.penup();t.goto(random.randint(-250,250),random.randint(-200,250));
    t.dot(5)

turtle.done()