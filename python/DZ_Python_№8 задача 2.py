# DZ_Python_№8 задача 2
# Пользователь вводит с клавиатуры числа.
# Если число больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative»,
# если равно нулю «Number is equal to zero».
# Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»

number = int(input("Введите число: "))

while number != 7:
    if number < 0:
        print("Number is negative")
    elif number > 0:
        print("Number is positive")
    elif number == 0:
        print("Number is equal to zero")
    number = int(input("Введите число: "))

print("Good bye!")
