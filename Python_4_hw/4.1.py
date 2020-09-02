"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

# print(argv)


def salary_calc(time_spend, time_cost, bonus):
    return int(time_spend) * int(time_cost) + int(bonus)


print('Работник заработал: ', salary_calc(argv[1], argv[2], argv[3]))