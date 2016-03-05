# NOTES: LISTS

# CREATING LISTS
# We create a list using a list of comma seperated values between square
# brackets.
L1 = [1,2,3,4,5]
print("L1 is", L1)

# ACCESSING LISTS
# We can access an item in a list by referencing the index of that item
# Note: The first item is located at index 0
second_item = L1[1]
print("The second item is", second_item)

# SLICING LISTS
# Lists can be sliced using the following notation
list1 = L1[:2]   # start --------> 2nd index
list2 = L1[2:3]  # 2nd index ----> 3rd index
list3 = L1[3:]   # 3rd index ----> end
print("list1 is", list1)
print("list2 is", list2)
print("list3 is", list3)

# ADDING LISTS
print("(list1 + list2 + list3) is", list1 + list2 + list3)

# LIST ITERATION
for i in range(0, len(L1)):
    print(L1[i])

for x in L1:
    print(x)

# EXERCISE 1: Write a function that returns the largest element in a list.
largest = 0
L2 = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(L2)):
    if L2[i] > largest:
        largest = L2[i]
print(largest)

# EXERCISE 2: Write a function that checks whether an element occurs in a list.
search_for = 10
L3 = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(L3)):
    if L3[i] == search_for:
        print("Found it!!!!")

# EXERCISE 3: Write a function that computes the running total of a list.
total = 0
L4 = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(L4)):
    total = total + L4[i]
print(total)
