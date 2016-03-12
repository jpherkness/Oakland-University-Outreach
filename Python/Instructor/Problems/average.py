# Average = Sum / Total number of elements

# Write a definition that takes three numbers and prints their average.
def average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print("The avarage is", average)
average(1,2,3)

# Write a definition that takes a list of numbers and prints their
# average.
def average_of_list1(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total = total + num
    average = total / len(list_of_numbers)
    print("The avarage is", average)

def average_of_list2(list_of_numbers):
    average = sum(list_of_numbers) / len(list_of_numbers)
    print("The avarage is", average)

average_of_list1([1, 2, 3, 4, 5, 6])
average_of_list2([1, 2, 3, 4, 5, 6])
