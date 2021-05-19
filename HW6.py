# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
start = int(input('Введите количество километров, которое пробежал спортсмен в первый день: '))
finish = int(input('Введите количество километров, которое хочет достичь спортсмен: '))
a = 1
while True:
    if start >= finish:
        break
    if start < finish:
        print('В {} день результат: {:.2f} км'.format(a, start))
        start = 0.1 * start + start
        a = a + 1
        continue
print('Спортсмен достигнет намеченного результата на {} день c результатом {:.2f} километра'.format(a, start))