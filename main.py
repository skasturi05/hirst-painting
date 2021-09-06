# import colorgram
import random
from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()
screen.colormode(255)
tur.hideturtle()

# colors = colorgram.extract('image.jpg', 136)
# color_list = []
# for value in range (len(colors)):
#     my_color = colors[value]
#     rgb = my_color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     color_tuple = (red, green, blue)
#     color_list.append(color_tuple)
#
# print(color_list)
color_list = [(1, 12, 31), (53, 25, 17),
              (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24),
              (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163),
              (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147),
              (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0), (29, 84, 92),
              (228, 174, 166), (186, 190, 201), (73, 73, 39)]
for row in range(10):
    tur.penup()
    tur.goto(-225, -200 + (row * 50))
    for column in range(10):
        current_color = random.choice(color_list)
        tur.dot(20, current_color)
        tur.penup()
        tur.forward(50)

    tur.setheading(270)
    tur.penup()
    tur.setheading(0)





screen.exitonclick()
