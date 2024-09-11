import turtle as t
from turtle import Turtle, Screen
import random

tim = t.Turtle()
t.colormode(255)
t.penup()
t.hideturtle()
t.setheading(255)
t.speed("fastest")
t.forward(300)
t.setheading(0)

colors_ = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
           (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
           (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
           (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205),
           (223, 178, 169)]


def hirst_(num_of_dots):
    for _ in range(1, num_of_dots + 1):
        t.dot(20, random.choice(colors_))
        t.forward(50)
        if _ % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)


hirst_(100)

screen = Screen()
screen.exitonclick()
