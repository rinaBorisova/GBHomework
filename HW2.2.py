# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = []

while True:
    a = input('Введите элемент списка, для выхода нажмите ex: ')
    if a.title() == 'Ex':
        break
    list.append(a)
    print(list)

print('Теперь мы перемешаем элементы полученного списка: 1й со 2м, 3й с 4м и тд. Получился следующий список: ')
try:
    for i in range(0, len(list), 2):
        list[i], list[i+1] = list[i+1], list[i]
        # Это обмен значениями через кортежи из методички)) А вот цикл for пришлось еще погуглить
        print(list)
except IndexError:
    print('Последний элемент не был переставлен, так как нечетный')

# А вот обработкой IndexError я горжусь, так как сразу сообразила, что делать
