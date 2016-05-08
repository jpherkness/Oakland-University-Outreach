# INPUT
# -----
# In python we can use the input function to ask the user for some information.
# The string inside the parenthesis is called the prompt.

i = input("Enter something: ")


# EVALUATION
# ----------
# When we want to convert a string to a number we use the following function.

ten1 = eval("10")
ten2 = 10

# These two statements are the same
# This is very useful when you are trying to prompt the user for a number.

num = eval(input("Enter a number: "))

# EXERCISE 1: Simple Input
# 1. Prompt the user for their age, then print the result
# 2. Prompt the user for their name, then print the result
# 3. Prompt the user for their favorite food, then print the result
# -----------------------------------------------------------------
age = input("Enter your age: ")
name = input("Enter your name: ")
food = input("Enter your favorite food: ")

# EXERCISE 2: Area of a circle
# 1. Prompt the user for the radius of a circle.
# 2. Calculate the area of the circle.
# 3. Print the result.
# ----------------------------------------------
radius = float(input("Enter the radius: "))
area = 3.1415 * radius ** 2
print("The area of the circle with radius " + str(radius) + " is: ", area)

# EXERCISE 3: Volume of a Sphere
# 1. Prompt the user for the radius of a sphere.
# 2. Calculate the volume of the sphere
# 3. Print the result.
# ----------------------------------------------
radius = float(input("Enter the radius: "))
volume = (4/3) * 3.1415 * radius ** 3
print("The volume of a sphere with radius " + str(radius) + " is: ", volume)
