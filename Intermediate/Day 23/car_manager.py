import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEFT = 180

class Car(Turtle):
    def __init__(self, current_level):
        self.car_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * current_level-1)
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(LEFT)
        self.shapesize(stretch_wid=1, stretch_len=2)     
        self.speed("fastest")
        self.fillcolor(COLORS[random.randint(0, len(COLORS)-1)])   
        self.goto((320, random.randint(-240, 240)))
        
    
    def move(self):
        self.forward(self.car_speed)