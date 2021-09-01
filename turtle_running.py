import turtle
from turtle import Turtle,Screen
import random


is_race_on = False

color_list = ["red","blue","green","yellow","orange","purple"]
y_position = [-70,-40,-10,20,50,80]
turtle_id = []

screen = Screen()

# set up the height and the width of the pop-up window
screen.setup(width=500,height=400)

# alert window to make a bet before the race
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")



# ADD STATE : set for each turtle's properties and starting position
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_position[turtle_index])
    new_turtle.color(color_list[turtle_index])
    # create different turtle in array turtle_id
    turtle_id.append(new_turtle)

# if user_bet input:
if user_bet:
    is_race_on = True

while is_race_on:
    for eachTurtle in turtle_id:
        # check coordonné of the winning turtle
        if eachTurtle.xcor() > 230:
            winning_turtle = eachTurtle.pencolor()
            print(winning_turtle)
            if winning_turtle == user_bet:
                print("you won")

            else:
                print("you loose")
            is_race_on = False

        # create a randint speed for each turtles
        rand_distance = random.randint(0,10)
        eachTurtle.forward(rand_distance)


screen.exitonclick()
