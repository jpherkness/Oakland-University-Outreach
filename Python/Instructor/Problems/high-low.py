# Write a game where the computer picks a random number between 0 and 100,
# then prompts the user for a number. The computer should then notify the
# user whether the number is high, low, or correct. The user should keep
# guessing until they choose the correct number.
#
# To pick a random number between 'a' and 'b' use random.randint(a, b)
import random

computers_number = random.randint(0, 100)
correct = False
while(not correct):
    guess = eval(input("Enter a number: "))
    if(guess == computers_number):
        correct = True
        print("That is correct!")
    elif(guess < computers_number):
        print("Low...")
    else:
        print("High...")
