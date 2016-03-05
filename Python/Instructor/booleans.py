# NOTES: BOOLEANS

# Boolean operators (not and or)
bool_not = not True
bool_and = True and True
bool_or = True or False

# Comparison Operations
bool_less_than = 10 < 7
bool_greater_than = 3 > 5
bool_less_than_or_equal = 4 <= 2
bool_greater_than_or_equal = 8 >= 4
bool_equal = 9 == 9
bool_not_equal = 6 != 2

# EXERCISE 1: Fill out the following truth tables
#
#  | X | Y | X and Y |         | X | Y | X or Y  |         | X | not Y |
#  | T | T |    T    |         | T | T |    T    |         | T |   F   |
#  | F | T |    F    |         | F | T |    T    |         | F |   T   |
#  | T | F |    F    |         | T | F |    T    |
#  | F | F |    F    |         | F | F |    F    |

# EXERCISE 2: Simplify the following boolean conditions
bool_one = False or not True and True 							# False
bool_two = False and not True or True 							# True
bool_three = True and not (False or False) 						# True
bool_four = not not True or False and not True 					# True
bool_five = False or not (True and True) 						# False
bool_six = False or (False or True) and (True and not False) 	# True

# EXERCISE 3: Using each boolean operator, create a complex boolean that
# simplifies to false and another that simplifies to true.
bool_true = True
bool_false = False

# EXERCISE 4: Simplify the following boolean conditions
bool_one = False or (1 < 4) and True or (6 > 7) or not (4 != 4)	# True
bool_two = ((5 * 5) != 24) and not ((5 % 4) == 2) and (1000 > 2)# True
