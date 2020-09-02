a = 12.85
internal_list = [0, a, 2, 400]
result_list = [1, 2, 'aBc', 'cbDa', [0, a, 2, 400], 4.5, 12.56, None, False]
print(result_list)

i = 0
k = 0

for el in result_list:
    print(type(el), f'- is {i} from result_list')
    i += 1

for elem in internal_list:
    print(type(elem), f'- is {k} from internal_list')
    k += 1

print('Проверка типов окончена успешно')