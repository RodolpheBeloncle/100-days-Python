import turtle as turtle_module

import random
import colorgram
turtle_module.colormode(255)
tim = turtle_module.Turtle()
#colors = colorgram.extract('painting.jpg', 30)
#rgb_colors = []
# formatting in tupples different rgb colors
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r,g,b)
    #rgb_colors.append(new_color)
#print(rgb_colors)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
color_list = [(26, 109, 164), (194, 38, 81), (237, 161, 51), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 109, 58), (102, 197, 219), (205, 166, 30), (21, 58, 132), (212, 74, 91), (238, 89, 52), (142, 208, 226), (119, 192, 140), (6, 159, 88), (5, 186, 178), (106, 108, 198), (137, 29, 72), (98, 51, 36), (24, 154, 211), (228, 169, 188), (153, 213, 194), (175, 186, 220), (233, 174, 164), (31, 91, 94), (84, 46, 34), (36, 45, 82)]
number_of_dots = 100
tim.speed("fastest")
tim.penup()
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
#  --------- Angela solution -------------


# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
#
#
#
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()
