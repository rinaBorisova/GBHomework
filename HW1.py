# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран
print ('Это самый простой скрипт с переменными')
b = ' - это ваше число'
a = input ('Введите целое число: ')
print (a, b)

print ('Этот скрипт имеет небольшую логику')
name = input ('Введите свое имя: ')
friend_name = input ('Введите имя вашего друга: ')
age = input ('Введите ваш возраст: ')
friend_age = input ('Введите возраст вашего друга: ')
mid_age = (int(age) + int(friend_age))/2
print ('В среднем пользователям', name, 'и', friend_name, mid_age, 'лет')
