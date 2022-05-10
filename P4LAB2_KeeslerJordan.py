import turtle          
win = turtle.Screen()
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")

t.backward(100)
t.right(90)
t.forward(50)

for s in range (3):  
    t.right(90)
    t.backward(100)

t.penup()
t.pencolor("red")
t.forward(160)
t.left(90)
t.pendown()
t.forward(150)
t.right(90)
t.forward (100)
t.penup()
t.left(90)
t.backward(100)
t.pendown()
t.forward(10)
t.right(90)
t.forward(30)
t.right(90)
t.forward(58)
t.right(90)
t.forward(130)


    
win.mainloop()             # Wait for user to close window
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
