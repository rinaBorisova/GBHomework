# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

fisrt_list = []
while True:
    line = input('Введите значение, содержащееся в строке: ')
    if line == '':
        print(fisrt_list)
        exit()
    else:
        new_line = line + '\n'
        fisrt_list.append(new_line)

    with open('5.1.txt', 'w') as f:
        f.writelines(fisrt_list)