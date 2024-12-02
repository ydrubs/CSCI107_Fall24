"""In this lesson we will explore how to use multiple turtles for drawing on to the screen.
We create instance variables from the turtle class rather then using the generic class as in previous lessons.
"""
import turtle

## Create an instance of the turtle screen object
window = turtle.Screen()
window.setup(600,600)
window.bgcolor('yellow')

## Create an array to store multiple turtle objects
my_turtles = []

##Create and store turtles into the list
larry = turtle.Turtle()
larry.pensize(3)
larry.pencolor('purple')
larry.penup()
my_turtles.append(larry)


curly = turtle.Turtle()
curly.pensize(4)
curly.pencolor('blue')
curly.penup()
my_turtles.append(curly)

moe = turtle.Turtle()
moe.pensize(5)
moe.pencolor("red")
moe.penup()
my_turtles.append(moe)


## Send commands to each turtle individuals
larry.goto(-200,200)
curly.goto(200,200)
moe.goto(0,-200)

##Send commands to each turtle by looping through the list
for trtl in my_turtles:
    trtl.shape('turtle')
    trtl.pendown()
    for move in range(3):
        trtl.forward(50)
        trtl.right(120)



turtle.write("Turtle Power", align='center', font=('Verdana', 25, 'normal'))

##Define functions for keyboard presses
def up():
    larry.setheading(90)
    larry.forward(5)


def down():
    larry.setheading(270)
    larry.forward(5)


def left():
    larry.setheading(180)
    larry.forward(5)


def right():
    larry.setheading(0)
    larry.forward(5)

##Create a keypress listener and assosiate with a key
#Note that we are using the turtle graphic instance rather then an instance of a turtle
turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')


turtle.done()
