from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.right_score = 0
        self.left_score = 0
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(0, 200)
        self.write(f"{self.right_score} - {self.left_score}", align=ALIGNMENT, font=FONT )
        self.shapesize(20, 20)

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.write(f"{self.right_score} - {self.left_score}", align=ALIGNMENT, font=FONT )
    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.write(f"{self.right_score} - {self.left_score}", align=ALIGNMENT, font=FONT )