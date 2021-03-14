# DZ_Python_№8 задача 1
# Пользователь вводит с клавиатуры два числа.
# Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне,
# а также среднеарифметическое каждой группы.


number_first = int(input("Введите первое число: "))
number_last = int(input("Введите второе число: "))
count = 0
summa = 0

#подсчет cуммы и среднеарифметического чётных чисел
for i in range(number_first,number_last + 1):
    if i%2 == 0:
        count += 1
        summa += i
print("Сумма чётных чисел:",summa,"\nСреднеарифметическое чётных чисел:", summa/count)

count = 0
summa = 0
##подсчет cуммы и среднеарифметического нечётных чисел
for i in range(number_first, number_last + 1):
    if i%2 == 1:
        count += 1
        summa += i
print("Сумма нечётных чисел:",summa,"\nСреднеарифметическое нечётных чисел:",summa/count)

count = 0
summa = 0
#подсчет cуммы и среднеарифметического кратных 9
for i in range(number_first, number_last + 1):
    if i%9 == 0:
        count += 1
        summa += i
print("Сумма чисел кратных девяти:",summa,"\nСреднеарифметическое чисел кратных девяти:",summa/count)