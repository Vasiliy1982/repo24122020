# DZ_Python_№9 задача 1
# Пользователь вводит с клавиатуры две границы диапазона и число.
# Если число не попадает в диапазон, программа просит пользователя повторно ввести число,
# и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона,
# выделяя число восклицательными знаками. Например: 1 2 3 !4! 5 6 7

number_first = int(input("Введите первое число: "))
number_last = int(input("Введите второе число: "))

number_input = int(input("Введите число: "))

for i in range (number_first, number_last +1):
    while number_input < number_first  or number_input >number_last:
        number_input = int(input("Введите число: "))
    if i == number_input: print("!",i,"!", end="")
    else:print(i, end="")
