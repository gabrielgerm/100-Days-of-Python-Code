from turtle import Screen
from paddle import Paddle

RIGHT_PADDLE_POSITION = (580, 0)
LEFT_PADDLE_POSITION = (-580, 0)

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)

screen.update()

screen.listen()
screen.onkey(right_paddle.up_paddle, "Up")
screen.onkey(left_paddle.up_paddle, "w")
screen.onkey(right_paddle.down_paddle, "Down")
screen.onkey(left_paddle.down_paddle, "s")

game_is_on = True
while game_is_on:
    screen.update()
#     if ball.positionx > or < :
        



screen.exitonclick()