# NOTES: BOOLEANS

# EXERCISE 1: Fill out the following truth tables
#
#  | X | Y | X and Y |         | X | Y | X or Y  |         | X | not Y |
#  | T | T |    ?    |         | T | T |    ?    |         | T |   ?   |
#  | F | T |    ?    |         | F | T |    ?    |         | F |   ?   |
#  | T | F |    ?    |         | T | F |    ?    |
#  | F | F |    ?    |         | F | F |    ?    |

# EXERCISE 2: Simplify the following boolean conditions
bool_one = False or not True and True
bool_two = False and not True or True
bool_three = True and not (False or False)
bool_four = not not True or False and not True
bool_five = False or not (True and True)
bool_six = False or (False or True) and (True and not False)

# EXERCISE 3: Using each boolean operator, create a complex boolean that
# simplifies to false and another that simplifies to true.
bool_true = True
bool_false = False

# EXERCISE 4: Simplify the following boolean conditions
bool_one = False or (1 < 4) and True or (6 > 7) or not (4 != 4)
bool_two = ((5 * 5) != 24) and not ((5 % 4) == 2) and True or (1000 < 2)
