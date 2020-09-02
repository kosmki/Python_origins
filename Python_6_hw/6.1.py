"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
2 секунды, третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    def __init__(self):
        self._color = None
        self._history = self._color

    def running(self, switch):
        colors = ['красный', 'жёлтый', 'зелёный', 'жёлтый', 'красный']
        if not self._color and switch == 'красный':
            self._color = switch
            self._history = switch
            print(f'Загорелся {self._color}!')
        elif self._color == 'жёлтый' and self._history == 'зелёный' and switch == 'красный':
            sleep(2)
            self._color = switch
            self._history = switch
            print(f'Загорелся {self._color}!')
        elif (self._color == 'красный' or self._color == 'зелёный') and switch == 'жёлтый':
            sleep(7)
            self._color = switch
            print(f'Загорелся {self._color}!')
        elif self._color == 'жёлтый' and self._history == 'красный' and switch == 'зелёный':
            sleep(2)
            self._color = switch
            self._history = switch
            print(f'Загорелся {self._color}!')
        else:
            if self._color == 'жёлтый':
                print(f'До жёлтого был {self._history}. После \
                                                    {colors[colors.index(self._history) + 2]}!')
            elif not self._color:
                print('Первый "красный"!!!')
            else:
                print(f'После {self._color} будет {colors[colors.index(self._color) + 1]}!')

    def get_color(self):
        print(self._color)


traffic = TrafficLight()
traffic.running('жёлтый')
traffic.running('красный')
traffic.running('зелёный')
traffic.running('жёлтый')
traffic.running('зелёный')
traffic.get_color()  # текущий цвет красный