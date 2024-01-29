from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
all_turtles = []
for turtle_num in range(0, 6):
    toni = Turtle(shape="turtle")
    all_turtles.append(toni)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

bottom_turtle_x = -880
bottom_turtle_y = -150
for turtle_position in range(0, len(all_turtles)):
    all_turtles[turtle_position].fillcolor(colors[turtle_position])
    all_turtles[turtle_position].speed(4)
    all_turtles[turtle_position].shapesize(2, 2)
    all_turtles[turtle_position].up()
    all_turtles[turtle_position].goto(x= bottom_turtle_x, y=bottom_turtle_y)
    bottom_turtle_y += 60

if user_bet:
    is_race_on = True


winner = ''
while is_race_on:
    for turtle_position in range(0, len(all_turtles)):
        all_turtles[turtle_position].forward(random.randint(0, 20))
        if all_turtles[turtle_position].pos()[0] >= 860:
            winner = all_turtles[turtle_position]
            is_race_on = False

if user_bet == winner.fillcolor():
    print("You won!")
else:
    print("You lost!")

print(f"The winner is {winner.fillcolor()}!" )
screen.exitonclick()