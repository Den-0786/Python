import turtle 
from turtle import Turtle, Screen
import random


t = Turtle()
t.pensize(5)
t.hideturtle()
t.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

directions = [0, 90, 180, 270]
for _ in range(200):
    t.forward(20)
    t.setheading(random.choice(directions))
    t.color(random_color())



screen = Screen()
screen.exitonclick()