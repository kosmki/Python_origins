"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

from itertools import count
from random import randint


list1 = []

for el in count(3):
    if el > 10:
        break
    else:
        list1.append(el + randint(1, 10)*el)

print(list1)

with open('qwe.txt', 'w', encoding='utf-8') as f:
    # print(' '.join(map(str, list1)), file=f)
    f.write(' '.join(map(str, list1)))

with open('qwe.txt', 'r', encoding='utf-8') as s:
    lst = s.read().split()
    print(sum(map(int, lst)))