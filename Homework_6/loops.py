# Задача 1.Напишіть програму, яка виведе всі числа зі списку, які поділяються на задане число
# Число задавати з клавіатури

first_list_of_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 87, 98, 112]
divide_list_of_numbers = []
users_number = int(input('Print your number here: '))

for number_first in first_list_of_numbers:
    if number_first % users_number == 0:
        divide_list_of_numbers.append(number_first)

if divide_list_of_numbers:
    print(f'{users_number} is divisible by a list: {divide_list_of_numbers} without a remainder')
else:
    print(f'{users_number} is not divisible by any number from the list: {first_list_of_numbers} without a remainder.')

# Задача 2.Написати програму, яка знайде перше непослідовне число у списку
# Список задати у самій програмі у вигляді: list = [1, 5, 68, 0]
# У ньому може бути скільки завгодно елементів
# Наприклад, дано список [1,2,3,4,6,7,8]
# Відповіддю буде число 6. Якщо список послідовний, вивести відповідне повідомлення

second_list_of_numbers = [1, 2, 3, 4, 5, 6, 8]
# Variable to store the previous number
prev_number_from_list = second_list_of_numbers[0]
# Variable to store the next expected number
expected_number = prev_number_from_list + 1
# Flag to track whether a non-consecutive number was found
found_gap = False

# Iterate over numbers in the list, starting from the second
for number_second in second_list_of_numbers[1:]:
    if number_second != expected_number:  # If the current number is not equal to the expected number
        print(f'\nFirst non-consecutive number: {number_second}\n')
        found_gap = True
        break
    prev_number_from_list = number_second
    expected_number += 1

if not found_gap:
    print(f'\nThe list: {second_list_of_numbers} consists of consecutive numbers\n')

# Задача 3.Написати цикл, який виведе
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for line in range(1, 6):  # Loop for lines 1 to 5
    for number_third in range(1, line + 1):  # Loop for numbers from 1 to line
        print(number_third, end=' ')  # Print a number with a space at the end of the line
    print()  # Go to a new line after each line of numbers
