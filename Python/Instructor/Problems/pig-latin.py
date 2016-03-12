# Pig Latin is a language, where you move the first letter of the word to the
# end and add "ay." So "Python" becomes "Ythonpay".
#
# 1. Ask the user to input a word in English.
# 2. Make sure the user entered a valid word.
# 3. Convert the word from English to Pig Latin.
# 4. Display the translation result.
original_word = input("Enter a word: ")
if len(original_word) > 0:
    original_word = original_word.lower()
    new_word = original_word[1:len(original_word)] + original_word[0] + 'ay'
    new_word = new_word.title()
    print(new_word)
