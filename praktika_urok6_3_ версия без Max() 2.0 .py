#praktika_urok6_3

print("Введите четыри положительных числа")
number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
max_number = number1
nomer = 0
if max_number < number2:
    max_number = number2
    nomer = 2
else:
    nomer = 1
if max_number < number3:
    max_number = number3
    nomer = 3
if max_number < number4:
    max_number=number4
    nomer = 4
print("число за номером",nomer,"самое большое")
#print(max_number)
