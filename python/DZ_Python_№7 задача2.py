# Урок 7 Задача 2
# Задача 2
# Пользователь вводит с клавиатуры два числа. Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.


number1 = int(input("Введите начало диапазона:"))
number2 = int(input("Введите конец диапазона:"))
kratn7 = 0
kratn5 = 0
chetchik_krat5 = 0
summa = 0

print("\nКратные семи:")
for i in range(number1, number2 + 1):
    summa += 1
    kratn7 = summa % 7
    if kratn7 == 0:
        print(summa," ", end='')

print("\nKоличество кратных пяти:")

for i in range(number1,number2+1):
    summa += 1
    kratn5 = summa % 5
    if kratn5 == 0:
        chetchik_krat5 += 1
print(chetchik_krat5, " ", end='')

print("\nПо возрастанию")
for i in range(number1,number2+1):
    print(i," ", end='')
    i+=1

print("\nПо убыванию")

number2 = number2+1
while number2 > number1:
    number2 = number2 - 1
    print(number2, " ", end='')



