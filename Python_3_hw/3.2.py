"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
birth_year = int(input('Введите Ваш год рождения: '))
city = input('Введите Ваш город: ')
email = input('Введите Ваш емэйл: ')
tel = input('Введите Ваш телефон: ')


def user_data(name, surname, birth_year, city, email, tel):
    print(f"name - {name}; surname - {surname}; birth_year - {birth_year}; city - {city}; email - {email}; tel - {tel}")


user_data(name=name, surname=surname, birth_year=birth_year, city=city, email=email, tel=tel)
