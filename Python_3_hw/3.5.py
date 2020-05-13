"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def ultra_sum():
    user_nums = input('Введите числа через пробел: ')
    main_list_sum = sum(list(map(int, user_nums.split())))  # распаковка и суммирование

    print(main_list_sum)

    while True:
        user_nums_2 = input('Введите еще числа через пробел или Q для выхода: ')
        if user_nums_2.lower() == "q":  # условие если пользовател ввел q
            print(main_list_sum)
            break
        elif user_nums_2[-1::].lower() == "q":  # условие если в конце списка есть q
            extra_list = sum(list(map(int, user_nums_2[0:-1:].split())))  # отделяем числа от последней q
            print(main_list_sum + extra_list)
            break

        additional_list_sum = sum(list(map(int, user_nums_2.split())))
        print(main_list_sum + additional_list_sum)
        main_list_sum = additional_list_sum + main_list_sum

    return main_list_sum


ultra_sum()