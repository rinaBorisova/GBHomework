# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

a = float(input('Введите любое число: '))
b = float(input('Введите другое любое число: '))
c = float(input('Введите еще одно любое число: '))

def my_func(a,b,c):
    sum = a + b + c - min([a, b, c])
    return sum

summ = my_func(a,b,c)
print('Сумма двух наибольших чисел:', summ)