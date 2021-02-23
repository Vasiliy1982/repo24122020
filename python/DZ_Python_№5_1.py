# DZ_Python_№5_1
print("Необходимо ввести три числа")
number1 = int(input("Введите первое число:"))
number2 = int(input("Введите второе число:"))
number3 = int(input("Введите третье число:"))
print("Если хотите получить сумму нажмите 1, произведение - 2")
summa = number1+number2+number3
proizvededie = number1*number2*number3
choice = input()
if choice == "1":
    print(summa)
if choice == "2":
    print(proizvededie)