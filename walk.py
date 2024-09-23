from turtle import Turtle, Screen
import  turtle
import random
timmy = Turtle()
timmy.speed("fastest")
timmy.pensize(10)

turtle.colormode(255)
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    

for _ in range(200):
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.color(random_color())


screen = Screen()
screen.exitonclick()