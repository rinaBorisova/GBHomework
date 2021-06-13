# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#
# Результат: [23, 1, 3, 10, 4, 11]

first_list = [43, 555, 3, 43, 79, 8, 22, 3, 98, 555, 72]
sec_list = [i for i in first_list if first_list.count(i) == 1]

print(f'Исходный список: {first_list}')
print(f'Новый список: {sec_list}')