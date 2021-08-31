
#def random_walk():
    #random_direction = random.choice(range(0, 360))
    #random_color()
    #timmy.forward(30)
    #timmy.setheading(random_direction)


########### Challenge 5 - Spirograph ########

#def draw_spirograph(size_of_gap):
    #for _ in range(int(360 / size_of_gap)):
        #timmy.color(random_color())
        #timmy.circle(100)
        #timmy.setheading(timmy.heading() + size_of_gap)

#draw_spirograph(5)




#def draw_shape(num_sides):
    #angle = 360 / num_sides
    #for _ in range (num_sides):
        #timmy.forward(100)
        #timmy.right(angle)

#for shape_side_n in range(3,11):
    #timmy.color(random.choice(colors))
    #draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()

