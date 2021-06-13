# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} начал движение'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул направо'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} {self.speed}км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}км/ч')

        if self.speed > 40:
            return f'превышением скорости {self.speed}км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}км/ч')

        if self.speed > 60:
            return f'превышением скорости {self.speed}км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



a1 = TownCar(190, 'Баклажан', 'Лада Седан', False)
a2 = TownCar(30, 'Зеленая', 'Пятнашка', False)
a3 = WorkCar(70, 'Оранжевый', 'Камаз', False)
a4 = SportCar(110, 'Красный', 'Тойота Супра', False)
a5 = TownCar(110, 'Черная', 'Камри 3.5', False)
a6 = PoliceCar(90, 'Серебристая', 'Лада Веста', True)

print(f'{a4.name} по цвету {a4.color}')
print(a3.stop())
print(a6.stop())
print(a1.stop())
print(f'Автомобиль {a3.name} заблокировал движение для {a6.name} и {a1.name}')
print(f'{a6.name} полицейская? {a6.is_police}')
print(a4.turn_left())
print(a5.turn_left())
print(a4.show_speed())
print(f'{a5.name} едет с {a5.show_speed()}')
print(a6.go())
print(a5.stop())
print(f'{a1.name} полицейская? {a3.is_police}')
