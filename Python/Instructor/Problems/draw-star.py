# Write a definition that tells a turtle to draw a star.
import turtle
def draw_star():
    for side in range(5):
        turtle.forward(50)
        turtle.right(144)
    turtle.exitonclick()

draw_star()
