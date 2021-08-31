from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear():
    tim.home()
    tim.clear()

screen.listen()


# on key space bar press use function move_forwards
screen.onkey(key="x",fun=move_forwards)
screen.onkey(key="w",fun=move_backwards)
screen.onkey(key="l",fun=counter_clockwise)
screen.onkey(key="r",fun=clockwise)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
