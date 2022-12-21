# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# for i in range(1, 20):


# def num(0):
#     print('.')
#     print('..')
#     print('...')
#     print('....')
# num()

""""
import turtle

a = turtle.getscreen()
b = turtle.Turtle()
turtle.bgcolor("pink")
turtle.title("Work")
# turtle.pen(pencolor="red", fillcolor="white", speed=8, pensize=2)
# turtle.begin_fill()
turtle.backward(320)
turtle.left(90)
turtle.forward(125)
turtle.right(90)
turtle.forward(320)
turtle.right(90)


turtle.forward(250)
turtle.right(90)
turtle.forward(320)
turtle.right(90)
turtle.forward(125)

turtle.done()

turtle.end_fill()
"""

# import turtle
#
# a = turtle.getscreen()
# t = turtle.Turtle()
# turtle.title("Happy Christmas")
# turtle.bgcolor("pink")
# b = input("What to paint?Circle or square?")
# turtle.pen(fillcolor="black", pensize=4, speed=2)
# turtle.begin_fill()
# if b == "Circle":
#     turtle.circle(90)
#     turtle.write("/!=")
# elif b == "Square":
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(105)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.write("*")
# turtle.end_fill()
#
# turtle.done()

import turtle

turtle.shape("turtle")
a = turtle.getscreen()
t = turtle.Turtle()
turtle.title("Glory to Ukraine")

turtle.pen(fillcolor="blue", pensize=4, speed=2)
turtle.begin_fill()
turtle.forward(350)
turtle.right(90)
turtle.forward(125)
turtle.right(90)
turtle.forward(350)
turtle.end_fill()
turtle.pen(fillcolor="yellow", pensize=4, speed=2)
turtle.begin_fill()
turtle.right(90)
turtle.forward(125)
turtle.backward(250)
turtle.right(90)
turtle.forward(350)
turtle.left(90)
turtle.forward(125)
turtle.end_fill()

turtle.done()


