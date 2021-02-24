#praktika_urok6_3

print(" Введите четыри положительных числа")
number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
max_number = number1
if max_number < number2:
    max_number = number2
if max_number < number3:
    max_number = number3
if max_number < number4:
    max_number=number4

print(max_number)