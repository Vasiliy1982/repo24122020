# DZ_Python_№10 задача 1
# Показать на экран таблицу умножения в диапазоне, указанном пользователем. Например, если пользователь
# указал 3 и 5, таблица может выглядеть так
# 3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30
# .....................................................................................
# 5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50.


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

for i in range(number1, number2 +1):
    for j in range(1,10 +1):
        print(i,"*",j,"=",i*j)