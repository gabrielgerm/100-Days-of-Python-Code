from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.ball_x_move = 2
        self.ball_y_move = 2
        
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.fillcolor("white")
        
    def move_ball(self):
        next_x = self.xcor() + self.ball_x_move
        next_y = self.ycor() + self.ball_y_move
        self.setposition((next_x, next_y))

    def wall_bounce(self):
        self.ball_y_move *= -1

    def paddle_bounce(self):
        self.ball_x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.ball_x_move *= -1
        self.ball_y_move *= -1
