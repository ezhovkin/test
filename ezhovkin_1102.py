# Домашнее задание
# Работа с функциями и данными
#
# Цель:
# применить на практике пройденные на двух предыдущих семинарах темы
# использовать подходящие для решения задачи типы данных и применить нужные методы
# использовать операторы ветвления (if) и цикла (while, for)
# создать собственные функции

# Описание/Пошаговая инструкция выполнения домашнего задания:

# 1. Вводится целое число (любого размера). Написать функцию, которая разобьет это число на разряды символом "пробел", Функция возвращает тип данных str
# 1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976`

#Вариант 1
# s = 1234567890
# s = str(s)
# s5 = ''
# b = len(s)
# n = (b % 3)
# while b > 3:
#     s5 += s[-b:-b + n] + ' '
#     b -= n
#     n = 3
#
# s5 += s[-b:]
# print('Ответ:', s5)

#Ответ: 1 234 567 890

#Вариант 2

# s = 1234567890
# s = str(s)
# s5 = ''
# b = len(s)
# s = s[::-1]
# for i in range(len(s)):
#     s5 += s[i]
#     if (i + 1) % 3 == 0:
#         s5 += ' '
# s5 = s5[::-1]
# print('Ответ:', s5)

#Ответ: 1 234 567 890

#Вариант 3

# s = 1234567890
# s5 = f'{s:,}'
# s5 = s5.replace(',', ' ')
# print(s5)

#1 234 567 890

# 2. Написать функцию, которая заменяет принимает строку текста и изменяет снейк_кейс на КамелКейс и наоборот
# my_first_func -> MyFirstFunc, AnotherFunction -> nother_function

def sk_kk(string):
    string = string.replace('_', ' ')
    string = string.title()
    string = string.replace(' ', '')
    print(string)


string = "my_first_func"
#sk_kk(string)

def kk_sk(string):
    s5 = string[0].swapcase()
    for i in range(1, len(string)):
        if string[i].isupper():
            s5 += '_' + string[i].swapcase()
        else:
            s5 += string[i]
    print(s5)


string = "MyFirstFunc"
#kk_sk(string)

# 3. Написать функцию, которая принимает на вход квадратное уравнение (одной строкой) и возвращает его корни, либо сообщает, что их нет
# "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7

def quadratic_equations(a):
    a = a.replace(' ', '')
    b = 0
    summands = []
    for i in range(len(a)):
        if i != 0 and (a[i] == '-' or a[i] == '+' or a[i] == '='):
            summands.append(a[b:i])
            b = i
    # Ищем в списке коэффициенты
    # ['-x**2', '-11*x', '+28']
    for summand in summands:
        if summand.startswith('+'): summand = summand[1:]
        if 'x**2' in summand:
            parts = summand.split('x**2')
            if parts[0] == '':
                coefficient_a = 1
            elif '*' in parts[0]:
                partsin = parts[0].split('*')
                if partsin[0].startswith('+'):
                    coefficient_a = partsin[0][1:]
                else:
                    coefficient_a = partsin[0]
                coefficient_a = int(coefficient_a)
            else:
                if parts[0] == '-':
                    coefficient_a = -1
                elif parts[0] == '+':
                    coefficient_a = 1
                elif parts[0].startswith('+'):
                    coefficient_a = parts[0][1:]
                else:
                    coefficient_a = parts[0]
                coefficient_a = int(coefficient_a)
        elif 'x' in summand:
            parts = summand.split('x')
            if parts[0] == '':
                coefficient_b = 1
            elif '*' in parts[0]:
                partsin = parts[0].split('*')
                if partsin[0].startswith('+'):
                    coefficient_b = partsin[0][1:]
                else:
                    coefficient_b = partsin[0]
            else:
                if parts[0].startswith('+'):
                    coefficient_b = parts[0][1:]
                elif parts[0] == '-':
                    coefficient_b = -1
                else:
                    coefficient_b = parts[0]
            coefficient_b = int(coefficient_b)
        else:
            coefficient_c = summand
            coefficient_c = int(coefficient_c)
    # Считаем Дискриминант
    # D = b**2−4ac
    print(f'a = {coefficient_a}, b = {coefficient_b}, c = {coefficient_c}')
    discriminant = coefficient_b ** 2 - 4 * coefficient_a * coefficient_c
    print(f'D = {discriminant}')
    # Выбираем вариант решения
    if discriminant > 0:
        print("D>0")
        x_1 = round((-coefficient_b + (discriminant ** 0.5)) / (2 * coefficient_a), 2)
        x_2 = round((-coefficient_b - (discriminant ** 0.5)) / (2 * coefficient_a), 2)
        print(f'Ответ: x1={x_1}, x2={x_2}')
    elif discriminant == 0:
        print("D=0")
        x = round((-coefficient_b) / (2 * coefficient_a), 2)
        print(f'Ответ: x={x}')
    else:
        print("D<0")
        print(f'Ответ. Уравнение не имеет решения')


a = "x**2 - 11*x + 28 = 0"
#quadratic_equations(a)


# 4. Шифр Цезаря. Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int). Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря. Написать вторую функцию, которая будет проводить обратный процесс (или написать одну, выполняющую оба действия)
# 'dog', 3 -> 'grj', 'python', 5 -> 'udymts'
