from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= Y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    race_is_on = True
while race_is_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won,{winning_color} is the winner")
            else:
                print(f"You have lost,{winning_color} is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
    
screen.exitonclick()