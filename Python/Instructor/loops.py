# NOTES: LOOPS

# Loops are used to repeat a section of code over and over again. THe two
# primary types of loops are for-loops and while-loops.

# WHILE LOOPS: A while loop repeats a section of code over and over again
# as long as some condition is true.
#
# while <condition>:
#     <statement>
#     <statement>
#     <statement>
counter = 0
while (counter < 10):
    print(counter)
    counter = counter + 1

# FOR LOOPS: A for loop is typically used to loop through a range of numbers.
#
# for <counter> in range(<start>, <tail>, <incrementor>):
#     <statement>
#     <statement>
#     <statement>
for counter in range(0, 10):
    print(counter)

# EXERCISE 1: Print all numbers from 0 to the users age
age = eval(input("Enter your age: "))
for a in range(age + 1):    # Note: We need to add 1 to age because it is
    print(a)                # exculusive.

# EXERCISE 2: Print all multiples of three between two numbers
start = 3
end = 1000
for i in range(start, end, 3):
    print(i)

# EXERCISE 3: Print n digits of the fibonacci sequence ( 1 1 2 3 5 8 ...)
# The next number is always the sum of the two previous numbers.
# n = (n - 1) + (n - 2)
n = 30
a = 0
b = 1
for i in range(n):
    print(a)
    old_a = a
    a = b
    b = b + old_a
