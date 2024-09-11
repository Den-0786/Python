import turtle as t
from turtle import Turtle, Screen
import random

tim = t.Turtle()
t.colormode(255)
t.speed("fastest")
t.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_circle(num_of_gaps):
    for _ in range(int(360/num_of_gaps)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + num_of_gaps)

draw_circle(5)


screen = Screen()
screen.exitonclick()
