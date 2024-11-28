from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong_Game")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))  

ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




game_is_on = True
while game_is_on:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect when paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
    if scoreboard.l_score == 15 and scoreboard.r_score < 15:
        game_is_on = False
        scoreboard.game_over()
        
    
    elif scoreboard.r_score == 15 and scoreboard.l_score < 15:
        game_is_on = False
        scoreboard.game_over()
    
screen.exitonclick()