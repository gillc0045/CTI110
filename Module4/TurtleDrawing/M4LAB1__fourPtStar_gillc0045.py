# Turtle drawing a four-pt star with squares and triangles
# CTI 110: Web, Pgm, & Db Foundation
# 22 Jun 2017
# Calvin Gill

# Initialize parameters for drawing
import turtle
win = turtle.Turtle()
turtle.bgcolor("black")
turtle.color("yellow")
poky = turtle.Turtle()

# Center star on the canvas
turtle.penup()
turtle.backward(100)
turtle.setheading(270)
turtle.heading()
270.0
turtle.backward(100)
turtle.pendown()

# Draw a square
sides = 200
for square in range (4):
    turtle.forward(sides)
    turtle.left(90)

# Add triangles unto sides of square
angle = 60
for triangles in range (4):
    turtle.right(angle)
    turtle.forward(sides)
    turtle.left(120)
    turtle.forward(sides)
    angle = 30

