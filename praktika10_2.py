#Пользователь вводит любое целое число больше 9.
# Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.

number = int(input("Введите число больше 9 и меньше 100:\n"))
if number <= 9 or number > 99:
    print("ERROR")

for i in number:
    if (number) != 3 and (number) != 6:
        print(number)



