# STRINGS
# ------------------------------------------------------------------------------
# A string is a sequence of characters.
s = "   Hello"

# ACCESSING CHARACTERS
# ------------------------------------------------------------------------------
# Each character is represented by a different index (or position)
# Note: The first index is 0, not 1
# |   |   |   | H | e | l | l | o |
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

first_character = s[0]  # 0 is the index
second_character = s[1] # 1 is the index

# STRING MODIFIERS
# ------------------------------------------------------------------------------
# There are a bunch of things you can do to strings
s = s * 5			        # Repeat the string multiple times
s = s + "   "               # Add strings together
length = len(s)             # Retrieve the length of a string
s = s.title()			    # Capitalizes the first character
s = s.upper()			    # Capitalizes each character
s = s.lower()			    # Makes each character lowercase
s = s.strip()			    # Removes any trailing or leading spaces
s = s.replace(" ", "_")     # Replace all substrings with a different substring

# EXERCISE 1:
# 1. Declare two string variables and assign them values
# 2. Add the two strings together and store the result in a third variable
# 3. Repeat the third string 3 times
# 4. Remove and leading or trailing spaces from the new string
# 5. Capitalize every character in the new string
# 6. Replace and occurrence of 'E' with '*'
# ------------------------------------------------------------------------------

# EXERCISE 2: Pig Latin is a language, where you move the first letter
# of the word to the end and add "ay." So "Python" becomes "Ythonpay".
# 1. Ask the user to input a word in English.
# 2. Make sure the user entered a valid word.
# 3. Convert the word from English to Pig Latin.
# 4. Display the translation result.
# ------------------------------------------------------------------------------
