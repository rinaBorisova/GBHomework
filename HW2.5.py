# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

print('Программа  выводит какой-то рейтинг, убывающими числами')
list = [7, 5, 3, 3, 2]
print('Текущий рейтинг: ', list)
# Расположить все числа по списку по убыванию
a = int(input('Введите новый элемент рейтинга: '))
list.append(a)
list.sort()
list.reverse()
str_list = [str(i) for i in list]
print(", ".join(str_list))
# Здесь пришлось загуглить, чтобы научиться красиво выводить рейтинг
# Не знаю, как реализовать условие про элементы с одинаковым значением(