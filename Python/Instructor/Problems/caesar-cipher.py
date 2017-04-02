# Write a program that allows the user to encrypt and decrypt a
# plain text message using the caesar cipher.
# ------------------------------------------------------------------------------
import string

#
# Function that prompts the user to either encrypt or decrypt a message.
#
def prompt():
    option = input("Would you like to encrypt (E) or decrypt (D) a message: ")
    message = input("Please input your message: ")
    key = eval(input("Please input your key: "))
    if option.upper() == "E":
        print(encrypt(message, key))
    elif option.upper() == "D":
        print(decrypt(message, key))
    else:
        print("I dont know what you mean...")

#
# Function that encrypts a plain text message with a given key.
#
def encrypt(plainText, key):
    # When beginning encryption on a message, we know nothing about the cipher text.
    cipherText = ""
    # Loop through each character in the plain text string.
    for character in plainText:
        cipherText += shiftCharacterInAlphabet(character, key)
    return cipherText

#
# Function that decrypts a cipher text message with a given key
#
def decrypt(cipherText, key):
    # When beginning decryption on a message, we know nothing about the plain text.
    plainText = ""
    # Loop through each character in the cipher text string.
    for character in cipherText:
        plainText += shiftCharacterInAlphabet(character, -1 * key)
    return plainText

#
# Function that shifts a character in the alphabet by a certain amount.
#
def shiftCharacterInAlphabet(character, amount):
    alphabet = list(string.ascii_uppercase)
    shiftedCharacter = ""
    try:
        # Find the index of the character in the alphabet
        index = alphabet.index(character.upper())
    except:
        return character

    # Calculate the shifted index of the letter using the key.
    shiftedIndex = (index + amount) % len(alphabet)
    # Find the shifted letter in the alphabet.
    shiftedCharacter = alphabet[shiftedIndex]
    return shiftedCharacter

# Program starts here
prompt()
