# DZ_Python_№10 задача 2
# Показать на экран все простые числа в диапазоне, указанном пользователем.
# Число называется простым, если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

simple = True
for i in range(number1, number2 +1):
    for j in range (2,i):
        if i%j == 0:
            simple = False
            break;
        else:
            simple = True

    if simple is True:print(i)