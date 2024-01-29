from turtle import Turtle, Screen

tim = Turtle()
tim.width(2)
tim.speed(10)
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def tilt_left():
    tim.left(10)

def tilt_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.up()
    tim.setpos((0,0))
    tim.setheading(0)
    tim.down()
    


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=tilt_left)
screen.onkey(key="d", fun=tilt_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
