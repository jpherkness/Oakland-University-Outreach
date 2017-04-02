# Returns binary string representation of a decimal number
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        rem = decimal % 2
        decimal = decimal // 2
        if rem == 0:
            binary = "0" + binary
        elif rem == 1:
            binary = "1" + binary
    return binary

# Returns decimal representation of a binary string
def binary_to_decimal(binary):
    decimal = 0
    for i in range(0, len(binary)):
        if binary[i] == "1":
            place_value = 2 ** (len(binary) - i - 1)
            decimal = decimal + place_value
    return decimal

# Call to the definition
print(decimal_to_binary(11))
print(binary_to_decimal("1011"))
