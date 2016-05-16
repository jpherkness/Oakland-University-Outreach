# NOTES: DEFINITIONS


# Definitions can be created using the following notation
def print_this_number(number):
    print(number)
# Note: 'number' is called a parameter. An parameter is a placeholder for
# information we do not know.

# We can then call the function using the following notation
print_this_number(20)
# Note: '20' is called an argument. An argument is the actual information sent
# to a function.

# Note: Definitions can have as many parameters as you want. To do so, just add
# a comma separating the parameters.


# EXERCISE 1: Write a function that takes a persons name as an argument and
# displays a message to greet them.
def greet(person):
    print("Hello,", person)


# EXERCISE 2: Write a function that takes two parameters, x and y, and prints
# the following sentence 'The sum of x and y is (x+y)', where (x+y) is the actual
# sum.
def sum_of_nums(x, y):
    s = x + y
    print("The sum of", x, "and", y, "is", s)
