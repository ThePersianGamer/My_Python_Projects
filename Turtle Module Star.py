#Drawing a star:
import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("light blue")
t.pencolor("orange")
t.pensize(10)
t.penup()
t.goto(-250, 10)
t.pendown()
for i in range(5):
    t.forward(500)
    t.right(144)
turtle.done()