"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))


def my_func(num_1, num_2, num_3):
    nums = [num_1, num_2, num_3]
    sort_nums = sorted(nums)
    print(sort_nums[1] + sort_nums[2])


my_func(num_1, num_2, num_3)
