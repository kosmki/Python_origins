"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

new_list = [k for k in range(99, 1001) if k % 2 == 0]
# print(new_list)

def my_f(prev_el, el):
    return prev_el * el


print(reduce(my_f, new_list))


