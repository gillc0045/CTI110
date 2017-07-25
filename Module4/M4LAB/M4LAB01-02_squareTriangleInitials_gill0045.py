# M4LAB01 -- code a program to draw a square and triangle
# M4LAB02 -- code a program to write my initials
# M4LAB01-02 -- Program displays a square, triangles and intials
# CTI 110: Web, Pgm, & Db Foundation
# 22 Jun 2017
# Calvin Gill

# Initialize parameters of turtle drawing
import turtle
win = turtle.Turtle()
turtle.bgcolor("black")
poky = turtle.Turtle()
poky.color("yellow")

# Variable Constants
a = 90     # a = 90 degree angle
b = 120    # b = 120 degree angle

# Center star on the canvas
poky.penup()
poky.backward(100)
poky.setheading(270)
poky.heading()
270.0
poky.backward(100)
poky.pendown()

# Draw a square
sides = 200
for square in range (4):
    poky.forward(sides)
    poky.left(a)

# Add triangles unto sides of square
angle = 60
for triangles in range (4):
    poky.right(angle)
    poky.forward(sides)
    poky.left(b)
    poky.forward(sides)
    angle = 30

# Initialize parameters of poky to write the letter "C"
poky.pensize(10)
poky.color("green")
poky.penup()
poky.forward(20)
poky.left(b)
poky.forward(130)
poky.pendown()
xC = 90     # xC = length of horizontal line
yC = 160    # yC = length of vertical line

# Draw the letter "C"
poky.backward(xC)
poky.right(a)
poky.forward(yC)
poky.left(a)
poky.forward(xC)

# Initialize parameters of poky to write the letter "G"
poky.penup()
poky.forward(45)
poky.left(a)
poky.forward(130)
poky.right(a)
#poky.forward(80)
poky.pendown()
xG = 70     # xG = length of horizontal line
yG = 100    # yG = length of vertical line
zG = yG*0.5 # zG = half of vertical line length

# Draw the letter "G"
poky.backward(xG)
poky.right(a)
poky.forward(yG)
poky.left(a)
poky.forward(xG)
poky.left(a)
poky.forward(zG)
poky.left(a)
poky.forward(xG*0.66)

