# Fix the following block of code, and fill in the blanks.
# As computer scientists, we must be able to debug (fix) broken code.

age = input("Enter your age: ")
if (age = 5)
    print(you are ___ years old)
else if (age > 16):
    print("you can drive")
else
    print("you are less than ___ and not ___")

# SOLUTION:
# age = eval(input("Enter your age: "))         # We want a number, not a string
# if (age == 5):                                # == is comparing, and we need :
#     print("you are 5 years old")              # Don't forget the quotes
# elif (age > 16):                              # elif not else if
#     print("you can drive")
# else:
#     print("you are less than 16 and not 5")
