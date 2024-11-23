"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


forwards = [100,76,82,25,50,40,31,35,164,103 ]
lefts = [ 90,70,33,68,93,51,26,73,82,78 ]
colors = [ 'red', 'pink', 'teal', 'yellow', 'brown', 'green', 'orange', 'purple', 'black', 'blue' ]

for  i in range(10):

    forward = forwards[i]
    left = lefts[i]
    color = colors [i]


    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  

