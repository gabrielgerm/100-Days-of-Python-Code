import time
from turtle import Screen
from snake import Snake

snake = Snake()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)    
    snake.snake_move()

screen.exitonclick()