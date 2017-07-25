# Turtle drawing of initials in my name
# CTI 110: Web, Pgm, & Db Foundation
# 22 Jun 2017
# Calvin Gill

import turtle
win = turtle.Turtle()
turtle.bgcolor("black")
turtle.color("green")
turtle.pensize(10)
poky = turtle.Turtle()

# Move the pen slightly to the left of the canvas
turtle.penup()
turtle.backward(90)
turtle.pendown()

a = 90     # a = 90 degree angle of block letters
x = 70     # x = horizontal distances
y = 120     # y = vertical distances
z = y*0.5  # z = half of vertical distance

# Draw the initial "C"
turtle.backward(x)
turtle.right(a)
turtle.forward(y)
turtle.left(a)
turtle.forward(x)

# Move the pen to the next letter
turtle.penup()
turtle.forward(50)
turtle.pendown()

# Draw the initial "P"
turtle.left(a)
turtle.forward(y)
turtle.right(a)
turtle.forward(x)
turtle.right(a)
turtle.forward(z)
turtle.right(a)
turtle.forward(x)

# Move the pen to the next letter
turtle.penup()
turtle.right(a)
turtle.forward(z)
turtle.right(a)
turtle.forward(2*x+50)
turtle.pendown()

# Draw the initial "G"
turtle.backward(x)
turtle.right(a)
turtle.forward(y)
turtle.left(a)
turtle.forward(x)
turtle.left(a)
turtle.forward(z)
turtle.left(a)
turtle.forward(x*0.66)
