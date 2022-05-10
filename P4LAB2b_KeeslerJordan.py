#CTI-110
#P4LAB2b
#Jordan Keesler
#9 MAY 2022
#






import random
import turtle


snowflake_poly = random.randint(0, 66)

turtle.bgcolor("red")

turtle.pensize(9)

for flake in range(snowflake_poly):
    colors = [ "blue","purple","teal","green","orange","white"]
    turtle.pencolor(colors [flake % 6])   
    ping = random.randint(50, 180)
    turtle.goto(0, flake)
    turtle.forward(ping)
    turtle.back(ping / 3)
    turtle.left(45)
    turtle.forward(25)
    turtle.back(25)
    turtle.left(-90)
    turtle.forward(25)
    turtle.back(25)
turtle.goto(0,0)


turtle.exitonclick()

