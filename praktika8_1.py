# Показать таблицу умножения для числа, введенного пользователем. Например, если пользователь вводит число 7, нужно показать:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# программа проверяет, что ввод правильный - от 2 до 10
number = int(input("Введите число для которого будет показана таблица умножения:\n"))
if number<2 or number>10:
    print("нужно ввести число от 2 до 10")
mnojetel = 1
proizvedenie =1
for i in range(10):

    proizvedenie = number*mnojetel
    mnojetel += 1
    print(number, "*", mnojetel,"=",proizvedenie)