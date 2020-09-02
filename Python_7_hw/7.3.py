"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных 2 клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, q):
        self.atoms = int(q)

    def __add__(self, other):
        return Cell(self.atoms + other.atoms)

    def __sub__(self, other):
        if self.atoms > other.atoms:
            return Cell(self.atoms - other.atoms)
        else:
            print('После вычитания клетка погибнет! Выберите другую клетку')

    def __mul__(self, other):
        return Cell(self.atoms * other.atoms)

    def __truediv__(self, other):
        return Cell(self.atoms // other.atoms)

    def make_order(self, maxvals):
        if self.atoms == maxvals:
            return '*' * self.atoms
        else:
            return ('*' * maxvals + '\n') * (self.atoms // maxvals) + '*' * (self.atoms % maxvals)


first = Cell(15)
second = Cell(4)
first = first - second  # 11
third = Cell(6)
second = second * third  # 15
print()
print(f'Состав {first.atoms} ячеек первой новой клетки:')
print(first.make_order(5))
print()
print(f'Состав {second.atoms} ячеек второй новой клетки:')
print(second.make_order(5))