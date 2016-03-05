# NOTES: INPUT

# In python you can use the input function to ask the user for some
# information. The thing inside the parenthesis is commonly refered to as
# the prompt.

i = input("Enter something: ")

# EXERCISE 1: Simple Input
# 1. Prompt the user for their age, then print the result
# 2. Prompt the user for their name, then print the result
# 2. Prompt the user for their favorite food, then print the result
age = input("Enter your age: ")
name = input("Enter your name: ")
food = input("Enter your favorite food: ")

# When we want to convert a string to a number we use the following
# functions
num = eval("10")
integer = int("10")			# Refered to as casting
float_ = float("3.1415")	# Refered to as casting

# This is very usefull when you are trying to promt the user for a number.
# Since the input function can only return a string
num = eval(input("Enter a number: "))

# EXERCISE 2: Area of a circle
# Write a Python program that prompts the user to enter a radius of a
# circle, then calculate and print the area.
radius = float(input("Enter the radius: "))
area = 3.1415 * radius ** 2
print("The area of the circle with radius " + str(radius) + " is: ", area)

# EXERCISE 3: Volume of a Sphere
# Write a Python program that prompts the user to enter a radius of a
# sphere, then calculate and print the volume.
radius = float(input("Enter the radius: "))
volume = (4/3) * 3.1415 * radius ** 3
print("The volume of a sphere with radius " + str(radius) + " is: ", volume)
