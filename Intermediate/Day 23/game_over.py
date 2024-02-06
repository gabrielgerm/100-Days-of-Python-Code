from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto((0, 0))
        self.write("GAME OVER!", align="center", font=FONT)