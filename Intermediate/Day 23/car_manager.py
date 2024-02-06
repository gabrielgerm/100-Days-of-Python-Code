import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=4)     
        self.speed("fastest")
        self.fillcolor(COLORS[random.randint(0, len(COLORS)-1)])   
        self.goto((320, random.randint(-240, 240)))
        self.setheading(LEFT)
    
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)