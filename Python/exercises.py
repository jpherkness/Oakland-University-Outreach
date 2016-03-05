# A sequential guide to python
# By Joseph Herkness
# 11 February 2016

def output():
	# The most basic form of output is the print function
	print("Hello World!")

	# You can use the print function to print multiple things
	print("My age is", 17, "...", "...", "...", "...")

def math():
	# Programming languages let us perform simple arithmatic operations.
	# QUESTION: What are some arithmatic operations?

	# Arithmatic Operators
	addition = 3 + 5              # 8
	subtraction = 4 - 3           # 1
	multiplication = 3 * 7        # 21
	division = 1 / 3              # 0.33333333
	modulus = 27 % 10             # 7
	integer_division = 27 // 10   # 2
	exponentiation = 2 ** 3       # 8

def variables():
	# A variable is a value that can change
	# Usually, we must specify the variables datatype
	# Data types tell us about what kind of information we are storing

	# Integer - from the Latin integer meaning "whole"
	x = 10
	y = -4
	age = 15

	# Float/Double - Float stands for floating point
	pi = 3.14159265

	# String
	name = "name"
	school = "Oakland University" 	# Strings can contain spaces
	date = "07/12/15"				# Strings can contain numbers

	# Boolean
	true = True
	false = False

	# EXERCISE 1:
	# 1. Create a variable to store your age
	# 2. Create a variable to store your name
	# 3. Create a variable to store height in feet

	# EXERCISE 2: Select the data type that fits best
	# Ex: Age - Integer
	# 1. Speed ----------------------- Float
	# 2. School ---------------------- String
	# 3. Number of Pets -------------- Integer
	# 4. High School Student --------- Boolean
	# 5. GPA ------------------------- Float
	# 6. Number of Twitter Followers - Integer
	# 7. Movie ----------------------- String
	# 8. Having Fun ------------------ Boolean
	# 9. Mass ------------------------ Float
	# 10. Date ----------------------- String

def strings():
	s = "   Hello"

	# There are a bunch of things you can do to with strings

	s = s * 5			# Repeat the string multiple times
	s = s + "   "   	# Add strings together
	length = len(s) 	# Retrieve the length of a string
	s.title()			# Capitalizes the first character
	s.upper()			# Capitalizes each character
	s.lower()			# Makes each character lowercase
	s.strip()			# Removes any trailing or leading spaces

def input_():
	# In python you can use the input function to ask the user for some
	# information. The thing inside the parenthesis is commonly refered to as
	# the prompt.

	i = input("Enter something: ")

	# EXERCISE 1: Simple Input
	# 1. Prompt the user for their age, then print the result
	# 2. Prompt the user for their name, then print the result
	# 2. Prompt the user for their favorite food, then print the result

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

def booleans():
	# Boolean operators
	# Order of operations : not and or
	bool_less_than = 10 < 7
	bool_greater_than = 3 > 5
	bool_less_than_or_equal = 4 <= 2
	bool_greater_than_or_equal = 8 >= 4
	bool_equal = 9 == 9
	bool_not_equal = 6 != 2
	bool_and = True and True
	bool_or = True or False
	bool_not = not True

	# EXERCISE 1: Fill out the following truth tables
	#
	#  | X | Y | X and Y |         | X | Y | X or Y  |         | X | not Y |
	#  | T | T |    T    |         | T | T |    T    |         | T |   F   |
	#  | F | T |    F    |         | F | T |    T    |         | F |   T   |
	#  | T | F |    F    |         | T | F |    T    |
	#  | F | F |    F    |         | F | F |    F    |

	# EXERCISE 2: Simplify the following boolean conditions
	bool_one = False or not True and True 							# False
	bool_two = False and not True or True 							# True
	bool_three = True and not (False or False) 						# True
	bool_four = not not True or False and not True 					# True
	bool_five = False or not (True and True) 						# False
	bool_six = False or (False or True) and (True and not False) 	# True

	# EXERCISE 3: Using each boolean operator, create a complex boolean that
	# simplifies to false and another that simplifies to true.
	bool_true = True
	bool_false = False

	# EXERCISE 4: Simplify the following boolean conditions
	bool_one = False or (1 < 4) and True or (6 > 7) or not (4 != 4)	# True
	bool_two = ((5 * 5) != 24) and not ((5 % 4) == 2) and (1000 > 2)# True

def password():
	# EXERCISE: Write a program that prompts the user for their password. If
	# their password matches the stored password then print 'Correct!'.
	# However, if their password does not match the stored password
	# print 'Incorrect!'

	original_password = "pa$$word"

	input_password = input("Enter a password: ")

	if input_password == original_password:
		print("Correct!")
	else:
		print("Incorrect!")

def area_of_circle():
	# Write a Python program which accept the radius of a circle
	# from the user and compute its area.

	radius = float(input("Enter the radius: "))
	area = 3.1415 * radius ** 2
	print("The area of the circle with radius " + str(radius) + " is: ", area)

def volume_of_sphere():
	# Write a Python program which accept the radius of a sphere
	# from the user and compute its volume.

	from math import pi
	radius = float(input("Enter the radius: "))
	volume = (4/3) * pi * radius ** 3
	print("The volume of a sphere with radius " + str(radius) + " is: ", volume)

def loops():
	# In general, statements are executed sequentially: The first statement in
	# a function is executed first, followed by the second, and so on. There
	# may be a situation when you need to execute a block of code several number
	# of times.

	# For loop
	for i in range(0, 5):
		print(i)

	for x in range(15):
		print(x)

	# While loop
	while True:
		print(True)

def multiples_of_three_while():
	# Find the sum of all the positive multiples of 3 below 1000.

	total = 0
	i = 3
	while i < 1000:
		total = total + i
		i = i + 3
		print(total)

def multiples_of_three_for():
	# Find the sum of all the positive multiples of 3 below 1000.

	total = 0
	for i in range(3, 1000, 3):
		total = total + i
	print(total)

def fibonacci():
	# Print the first 30 fibonacci numbers, and their sum.

	a = 0
	b = 1
	total = 0
	for i in range(30):
		print(i, ": ", a)
		total = total + a

		old_a = a
		a = b
		b = b + old_a

def pattern():
	# Write a python program that constructs the following pattern
	# *
	# * *
	# * * *
	# * * * *
	# * * * * *
	# * * * *
	# * * *
	# * *
	# *
	#
	# hint: You might want to use more than a single loop

	n=5;
	for i in range(n):
		print ('* ' * i)
	for i in range(n,0,-1):
		print('* ' * i)

def reverse():
	# Write a Python program that accept a word from the user and prints the
	# reverses of it.

	word = input("Enter a word: ")
	word_rev = ""
	for i in range(len(word) - 1, 0,-1):
		word_rev + word[i]
	print(word_rev)

def pyglatin():
	# Pig Latin is a language game, where you move the first letterof the word
	# to the end and add "ay." So "Python" becomes "ythonpay."
	#
	# 1. Ask the user to input a word in English.
	# 2. Make sure the user entered a valid word.
	# 3. Convert the word from English to Pig Latin.
	# 4. Display the translation result.

	original_word = input("Enter a word:")

	if len(original_word) > 0 and original_word.isalpha():
		original_word.lower()
		new_word = original_word[1:len(original_word)] + original_word[0] + 'ay'
		print(new_word)
	else:
		print('invalid word')

def even_odd():
	# Write a Python program that counts the number of even and odd
	# numbers from a series of given numbers.
	#
	# 1. Ask the user to input a list of comma seperated numbers
	# 2. Seperate those numbers into a list
	# 3. Determine wheter each number is even or odd.

	numbers = input('Enter a list of numbers (1, 2, 3): ')
	numbers = numbers.split(',')

	even = 0
	odd = 0

	for n in numbers:
		if(eval(n) % 2 == 0):
			even = even + 1
		else:
			odd = odd + 1
	print("Even: ", even)
	print("Odd: ", odd)
	''''''
def num_locator():
	# Write a Python program to find the numbers which are divisible by 7
	# and multiples of 5, between 1500 and 2700 (both included).

	for i in range(1500, 2701):
		if(i % 5 == 0 and i % 7 == 0):
			print(i)

def factorial(x):
	# Write a program to compute the factorial of a given number.
	# Hint: use a recursive function

    if x == 0:
        return 1
    return x * factorial(x - 1)

def lists():
	# Lists let us store a bunch of information in the same place

	names = ["Joey", "Josh", "Asem"]
	numbers = [1, 2, 4, 7, 10]
	bools = [True, False, True, True, False]

	# We can access each individual value using the index
	name = names[2]
	number = numbers[0]
	bool_ = bools[3]


def alphabetize():
	# Write a program that accepts a comma separated sequence
	# of words as input and prints the words in a comma-separated
	# sequence after sorting them alphabetically.

	words = input("Enter some comma seperated words: ")
	words = words.replace(" ", "")
	words = words.split(",")
	words.sort()
	words = ",".join(words)
	print(words)

def even_digits():
	# Write a program, which will find all such numbers between 1000 and 3000
	# (both included) such that each digit of the number is an even number.

	values = []
	for i in range(1000, 3001):
		s = str(i)
		if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
			values.append(s)
	print(",".join(values))
def count_digits_letters():
	# Write a program that accepts a sentence and calculate the
	# number of letters and digits.
	digits = 0
	letters = 0

	text = input("Enter a string with letters and digits: ")

	for c in text:
		if c.isdigit():
			digits = digits + 1
		elif c.isalpha():
			letters = letters + 1
	print("Digits:", digits, ",", "Letters:", letters)
