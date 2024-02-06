from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
UP = 90

class Player(Turtle):
    def __init__(self):  
        super().__init__()
        self.penup()
        self.shape("turtle")        
        self.speed("fastest")
        self.fillcolor("black")   
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        
    def move(self):
        self.forward(MOVE_DISTANCE)       

    def reset(self):
        self.goto(STARTING_POSITION)