
# Turtle Graphic
# CTI-110 P4LAB2 - Turtle Graphic
# 9 MAY 2022
# Jordan Keesler


import turtle

sides_of_shape = int(input('How many sides do you want your shape to have?\n'))
if sides_of_shape < 3:
    print('I said a shape')
elif sides_of_shape < 4:
    for sides in range(sides_of_shape): 
        turtle.forward(100)      
        turtle.left(120)      
elif sides_of_shape == 4:
    for sides in range(sides_of_shape):
        turtle.forward(100)
        turtle.right(90)        
else:
    for sides in range(sides_of_shape):
         turtle.forward(50)
         turtle.right(360 / sides_of_shape)
turtle.exitonclick()
