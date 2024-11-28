from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def game_over(self):
            self.goto(0, 0)
            self.write("Game over!!,", align=ALIGNMENT, font=FONT)
        
        
        
        
    