"""
HW5
Savchenko Kirill
"""
import random

# 1
print("FIRST TASK: ")
numbers = []

for i in range(10):
    numbers.append(random.randint(-10, 10))
print(numbers)


numbers_neg = 0

for num in numbers:
    if num < 0:
        numbers_neg += num
print(f"sum of negative numbers: {numbers_neg}")


numbers_even = 0
numbers_odd = 0
for num in numbers:
    if num % 2 == 0:
        numbers_even += num
    else:
        numbers_odd += num
print(f"sum of even numbers: {numbers_even}")
print(f"sum of odd numbers: {numbers_odd}")
"""
(нужно закомментировать предыдущую функцию чтоб сумма numbers_odd не суммировалась, or .copy)
# separate function:   
for num in numbers:
    if num % 2 != 0:
        numbers_odd += num
print(f"sum of odd numbers: {numbers_odd}")
"""


index_list = numbers[3:10:3]
prod = 1

for index in index_list:
    prod *= index
print(f"product of numbers whose index is equal to three: {prod}")


mini = min(numbers)
maxi = max(numbers)
index_mini = numbers.index(mini)
index_maxi = numbers.index(maxi)
prod = 1

if index_maxi > index_mini:  # Если включительно, то нужно убрать +1 из начального значения и перенести в конечное
    index_list = numbers[index_mini + 1:index_maxi]
elif index_maxi < index_mini:
    index_list = numbers[index_maxi + 1:index_mini]
for index in index_list:
    prod *= index
print(f"product of numbers between max and min indices: {prod}")

reverse_numbers = (numbers[::-1])

for number in numbers:
    if number > 0:
        index_fp = numbers.index(number)
        break
for number_r in reverse_numbers:
    if number_r > 0:
        index_lp = numbers.index(number_r)
        break
index_list = numbers[index_fp + 1: index_lp]
print(f"sum of numbers between the first and remaining positive elements: {sum(index_list)}")


# 2

print("SECOND TASK: ")
numbers = []
for i in range(10):
    numbers.append(random.randint(-10, 10))
print(numbers)

even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
print(f"even numbers: {even}")

odd = []
for number in numbers:      # опять же можно было сделать в один цикл
    if number % 2 != 0:
        odd.append(number)
print(f"odd numbers: {odd}")

zero = []
pos = []
neg = []
for number in numbers:
    if number < 0:
        neg.append(number)
    elif number > 0:
        pos.append(number)
    else:
        zero.append(number)
print(f"positive numbers: {pos}")
print(f"negative numbers: {neg}")
print(f"zero: {zero}")

#######################################################################################################################
print("ADDITIONAL TASK: ")

matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(10)]


print("matrix 10x10:")
for row in matrix:
    print(row)


main_diagonal_sum = sum(matrix[i][i] for i in range(10))
print(f"main diagonal sum: {main_diagonal_sum}")


anti_diagonal_values = [matrix[i][9 - i] for i in range(10)]
min_value = min(anti_diagonal_values)
max_value = max(anti_diagonal_values)
print(f"min value of side diagonal: {min_value}")
print(f"max value of side diagonal: {max_value}")


column_number = int(input("enter the number of the column (from 0 to 9): "))
print(f"column value {column_number}: {[row[column_number] for row in matrix]}")


swap_column1 = int(input("enter the number of first column to swap (from 0 to 9): "))
swap_column2 = int(input("enter the number of second column to swap (from 0 to 9): "))


if 0 <= swap_column1 < 10 and 0 <= swap_column2 < 10:
    for i in range(10):
        matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]
    print(f"matrix after column swap {swap_column1} and {swap_column2}:")
    for row in matrix:
        print(row)
else:
    print("number of column should be from 0 to 9.")
