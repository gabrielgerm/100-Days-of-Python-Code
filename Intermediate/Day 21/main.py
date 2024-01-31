import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

score_board = Scoreboard()
food = Food()
snake = Snake()

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

    if snake.snake_head.distance(food) < 15:
        food.food_refresh()
        snake.extend()
        score_board.score_refresh()

    if (
        snake.snake_head.xcor() > 280
        or snake.snake_head.xcor() < -280
        or snake.snake_head.ycor() > 280
        or snake.snake_head.ycor() < -280
    ):
        game_is_on = False
        score_board.game_over()

    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
screen.exitonclick()
