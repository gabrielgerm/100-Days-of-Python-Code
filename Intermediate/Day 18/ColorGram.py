# import colorgram

# colors = colorgram.extract("dot_paint.jpg", 20)

# my_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     my_colors.append((r, g, b))

# print(my_colors)
# [
#     (4, 5, 5),
#     (97, 70, 70),
#     (91, 107, 107),
#     (12, 14, 14),
#     (106, 40, 40),
#     (131, 130, 130),
#     (34, 20, 20),
#     (0, 1, 1),
#     (64, 69, 69),
# ]

import turtle as t
import random
t.colormode(255)

toni = t.Turtle()
color_list = [
    (4, 5, 5),
    (97, 70, 70),
    (91, 107, 107),
    (12, 14, 14),
    (106, 40, 40),
    (131, 130, 130),
    (34, 20, 20),
    (0, 1, 1),
    (64, 69, 69),
]

def new_line():
    toni.setpos(-212, toni.pos()[1]+50)

toni.hideturtle()
toni.speed(8)
toni.up()
toni.setheading(225)
toni.forward(300)
toni.setheading(0)

for i in range(0, 10):
    for j in range(0, 10):
        toni.dot(20, color_list[random.randint(0, len(color_list)-1)])        
        toni.forward(50)
    new_line()


screen = t.Screen()
screen.exitonclick()
