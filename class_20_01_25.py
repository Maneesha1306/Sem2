import turtle

star=turtle.Turtle()
star.color("black","purple")
star.begin_fill()
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)
star.end_fill()

def square(x,y):
    sq=turtle.Turtle()
    sq.penup()
    sq.forward(30)
    sq.pendown()
    sq.color("black","purple")
    sq.begin_fill()
    for i in range(4):
        sq.forward(100)
        sq.left(90)
    sq.end_fill()
    sq.write("Python turtle",font=("Comic Sans MS",20))

t=turtle.Turtle()
t.onclick(square)
turtle.done()