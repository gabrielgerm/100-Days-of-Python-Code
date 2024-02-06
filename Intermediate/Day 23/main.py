import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
from game_over import Game_over

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_list = []

screen.listen() 
screen.onkeypress(player.move, "Up")


game_is_on = True
times = 0
while game_is_on:
    times += 1
    if times%6 == 0:
        car_list.append(Car())

    for car in car_list:
        if player.distance(car) <= 50:
            distance = abs(player.ycor() - car.ycor())
            if distance <= 10:
                game_is_on = False
        else:
            car.move()

    
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.next_level()
        player.reset()

    time.sleep(0.1)    
    screen.update()

Game_over()
screen.update()

screen.exitonclick()
