"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = input('Пожалуйста, введите число: ')

#  %  - остаток от деления
#  // - целочисленное деление
i = 0
max_num = 0

while i >= 0:
    if max_num == 0:
        max_num = number[i]
    else:
        if number[i] > max_num:
            max_num = number[i]
        if i + 1 == len(number):
            break
        i += 1

print(max_num)

#
# number_1 = number % 10  # 4
# r_num_1 = number // 10  # 123
#
# number_2 = r_num_1 % 10  # 3
# r_num_2 = r_num_1 // 10  # 12
#
# number_3 = r_num_2 % 10  # 2
# r_num_3 = r_num_2 // 10  # 1
#
# number_4 =
#
# print(number_1, number_2, number_3)
#


# last_right = number % 10  # 5
# rest_number = number // 10  # 1234
#
# while rest_number > 0:
#     if last_right < last_right % 10:
#         last_right = last_right % 10
#         rest_number = rest_number // 10
#     if last_right > last_right % 10:
#         rest_number = rest_number // 10
#         continue
#
#
# print(last_right)
# print(number % 10)
# print(number // 10)

# while number > 0:


# stroka = int(number)
# print(stroka)
# #len_stroka = len(stroka)
# #print('Len = ', len_stroka)
#
# print(int(stroka[0]))
# print(stroka[1])
# print(stroka[2])
# print(stroka[3])
# print(stroka[4])
# #print(stroka[5])
#
# i = 0
# j = 1
#
# print('=' * 15)
#
# print(stroka[i + j])
# print(stroka[i])
#
# print(type(stroka[i]))
# #
# # while True:
# #     i += j
# #     if stroka[i + j] < stroka[i]:
# #         b = stroka[i + j]
# #     elif stroka[i] < stroka[i + j]:
# #         b = stroka[i]
# #     elif stroka[i + j] == stroka[i]:
# #         b = stroka[i]
# #     elif stroka[i + j] == 9:
# #         b = 9
# #         break
# #     elif stroka[i] == 9:
# #         b = 9
# #         break
#
# # print('Наибольшее число = ', b)
#
#
#
#
# # while True:
# #     i += 1
# #     if i <= len_stroka:
#


# print(number)
