'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__dict_income = {1: 13000, 2: 12000, 3: 96000, 4: 176000, 5: 205000, 6: 145000}  # оклад
        self.__dict_overincome = {1: 1000 * 2, 2: 3000 * 2, 3: 7000 * 2, 4: 12000 * 2, 5: 20000 * 2,
                                  6: 100000 * 2}  # премия
        self._income = 'Требуется расчет в классе Position'


class Position(Worker):

    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname}')

    def get_total_income(self):
        self._income = self._Worker__dict_income[self.position] + self._Worker__dict_overincome[self.position]
        print('Оклад + премия составляют', self._income)


worker_1 = Position('Антон', 'Подольский', 1)
worker_2 = Position('Костя', 'Дальнищий', 2)
worker_3 = Position('Георгий', 'Пышный', 3)
worker_4 = Position('Николай', 'Хмельнов', 4)
worker_5 = Position('Василий', 'Солодов', 5)
worker_6 = Position('Акакий', 'Акакиевич', 6)

worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()
worker_3.get_full_name()
worker_3.get_total_income()
worker_4.get_full_name()
worker_4.get_total_income()
worker_5.get_full_name()
worker_5.get_total_income()
worker_6.get_full_name()
worker_6.get_total_income()