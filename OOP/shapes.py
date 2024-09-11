from turtle import Turtle, Screen
import random
import turtle as t

tim = t.Turtle()
t.shape("turtle")
t.colormode(255)

#colors = ["orange red", "brown", "dark magenta", "deep pink", "coral", "sandy brown", "dark violet", "steel blue","royal blue","lawn green","orange"]

def draw_shape(num_sizes):
    angle = 360/num_sizes
    for _ in range(num_sizes):
        t.forward(100)
        t.right(angle)

def ram_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for shape_side_n in range(3, 11):
    t.color(ram_color())
    draw_shape(shape_side_n)
    
screen = Screen()
screen.exitonclick()