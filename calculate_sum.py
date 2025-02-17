# This program calculates the sum of all the numbers in a list
def calculate_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(calculate_sum([1, 2, 3, 4, 5]))