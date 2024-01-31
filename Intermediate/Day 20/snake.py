from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake_part()
        self.snake_head = self.snake_parts[0]
        
    def create_snake_part(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.fillcolor("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)    

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def snake_move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)
    
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_parts[0].setheading(180)       
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_parts[0].setheading(0)
