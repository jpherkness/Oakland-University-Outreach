# NOTES: TURTLES

# To use turtles we first have to import the package
import turtle

# You can change the appearance of the turtle using:
turtle.color("blue")
turtle.shape("turtle")
turtle.turtlesize(2)
turtle.width(5)

# EXERCISE 1: Make your turtle walk in a square.
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# EXERCISE 2: Using a loop make your turtle walk in a square.
for side in range(4):
    turtle.forward(100)
    turtle.right(90)

# EXERCISE 3: Make your turtle walk in an n-sided shape.
n = 5
for side in range(n):
    turtle.forward(50)
    turtle.right(360/n)

# EXERCISE 4: Make your turtle walk in a circle.
turtle.circle(100)  # 100 is the radius



turtle.exitonclick() # Closes the window when the user clicks on it
