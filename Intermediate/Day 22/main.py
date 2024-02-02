from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE_POSITION = (380, 0)
LEFT_PADDLE_POSITION = (-380, 0)
BALL_SPEED = 0.01


screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkeypress(right_paddle.up_paddle, "Up")
screen.onkeypress(left_paddle.up_paddle, "w")
screen.onkeypress(right_paddle.down_paddle, "Down")
screen.onkeypress(left_paddle.down_paddle, "s")

game_is_on = True
while game_is_on:
    screen.update()

    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.wall_bounce()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 360 or ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.paddle_bounce()
        BALL_SPEED *= 0.9

    if ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.reset()
        BALL_SPEED = 0.01
    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.reset()
        BALL_SPEED = 0.01

    ball.move_ball()    
    time.sleep(BALL_SPEED)

screen.exitonclick()