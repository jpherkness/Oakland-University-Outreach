# Write a definition that converts celcius to fahrenheit, and a definition that
# converts fahrenheit to celcius.
#
# Here are your equations:
# F = C * (9 / 5) + 32
# C = (F - 32) * (5 / 9)
def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius * (9 / 5) + 32
    print(fahrenheit)

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    print(celcius)

celcius_to_fahrenheit(37)
fahrenheit_to_celcius(100)
