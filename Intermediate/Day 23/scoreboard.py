from turtle import Turtle

SCOREBOARD_POSITION = (-200, 240)
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.current_level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def next_level(self):
        self.clear()
        self.current_level += 1
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.write(f"GAME OVER!", align="center", font=FONT)