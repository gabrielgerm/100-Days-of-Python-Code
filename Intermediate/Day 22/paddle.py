from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.fillcolor("white")        
        self.goto(position)
        self.setheading(UP)
    
    def up_paddle(self):
        self.forward(20)

    def down_paddle(self):
        self.backward(20)