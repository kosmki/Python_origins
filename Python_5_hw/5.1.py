"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


# import my_funcslib as mfl

with open('001.txt', 'w') as t:
    while True:
        text_input = input('Введите строку: ')
        if text_input == '':
            break
        t.write(text_input + '\n')