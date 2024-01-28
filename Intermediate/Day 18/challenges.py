import random
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
t.colormode(255)

def random_number():
    random_number = random.randint(0, 255)
    return random_number
def random_color_turtle():
    timmy_the_turtle.color((random_number(), random_number(), random_number()))


# challenge 1
# for i in range (0,4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# challenge 2
# for i in range (1,21):
#     timmy_the_turtle.forward(10)
#     if i%2 != 0:
#         timmy_the_turtle.up()
#     else:
#         timmy_the_turtle.down()


# challenge 3

# for i in range (3, 10):
#     times_draw = 0

#     random_color_turtle()
#     while times_draw != i:
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)
#         times_draw += 1
#     times_draw = 0
# timmy_the_turtle.forward(100)



# challenge 4
# orientation = [0, 90, 180, 270]
# timmy_the_turtle.pensize(20)
# timmy_the_turtle.speed(0)
# for i in range(0, 300):
#     random_color_turtle()
#     timmy_the_turtle.forward(50)
#     timmy_the_turtle.right(orientation[random.randint(0, 3)])
    


# challenge 5
# timmy_the_turtle.speed(0)
# for i in range(0, 90):
#     random_color_turtle() 
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.setheading(i*4)
#     print(timmy_the_turtle.heading())



screen = t.Screen()
screen.exitonclick()