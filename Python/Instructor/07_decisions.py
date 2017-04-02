# NOTES: DECISIONS
# ------------------------------------------------------------------------------
# Decision statements determine whether or not a block of code should be
# executed based on a boolean condition.

# IF STATEMENT
# ------------------------------------------------------------------------------
if 10 > 5:  # (10 > 5) is referred to as the condition
	print("10 is greater than 5")  # This statement will execute
# Note: notice the colon and indentations

# IF-ELSE STATEMENT
# ------------------------------------------------------------------------------
if 10 < 1:
	print("10 is less than 1")
else:
	print("10 is greater than 1")  # This statement will execute

# NESTED IF STATEMENT (IF-ELSEIF-ELSE STATEMENT)
# ------------------------------------------------------------------------------
if 10 < 10:
	print("10 is less than 10")
elif 10 == 10:
	print("10 is equal to 10")  # This statement will execute
else:
	print("10 is greater that 10")

# EXERCISE 1: Write a program that prompts the user for their password. If
# their password matches the stored password then print 'Correct!'.
# However, if their password does not match the stored password
# print 'Incorrect!'
# ------------------------------------------------------------------------------
original_password = "pa$$word"
input_password = input("Enter a password: ")
if input_password == original_password:
	print("Correct!")
else:
	print("Incorrect!")

# EXERCISE 2: Write a program that asks the user whether they want to solve for
# velocity, time, or distance. Based on their answer, prompt them for the
# appropriate inputs, and solve for that answer. When you're finished, display
# the answer to the user.
# ------------------------------------------------------------------------------
print("")
print("1. Velocity")
print("2. Distance")
print("3. Time")
print("")

# Asks the user to select on of the choices
choice = input("Which term would you like to solve for?: ")

# Based on that choice, ask for the unknowns, then solve for answer
if choice == "1":

	# Solve for velocity
	d = eval(input("Enter The Distance (meters):"))
	t = eval(input("Enter The Time (seconds):"))
	v = d / t
	print("The velocity is", v, "meters / second")

elif choice == "2":

	# Solve for distance
	v = eval(input("Enter The Velocity (meters/seconds):"))
	t = eval(input("Enter The Time (seconds):"))
	d = v * t
	print("The distance is", d, "meters")

elif choice == "3":

	# Solve for time
	d = eval(input("Enter The Distance (meters):"))
	v = eval(input("Enter The Velocity (meters/seconds):"))
	t = v / d
	print("The Time is", t, "seconds")
