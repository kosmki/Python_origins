"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func():
    user_text = input('Введите слова через пробел: ')
    user_text_list = list(map(str, user_text.split()))  # распаковка и вывод

    # print(user_text_list.capitalize())
    for i in user_text_list: print(i.capitalize())


int_func()
