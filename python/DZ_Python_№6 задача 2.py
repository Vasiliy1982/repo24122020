# Урок 6 Задача 2
# Зарплата менеджера составляет 200$ + процент от продаж.
# Продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%.
# Пользователь вводит с клавиатуры количество продаж за месяц для трех менеджеров.
# Программа должна рассчитать их зарплату, определить лучшего менеджера, начислить ему премию 200$,
# вывести на экран, сколько в итоге получит каждый менеджер

summa_prod1 = int(input("Введите сумму продаж первого менеджера:\n"))
summa_prod2 = int(input("Введите сумму продаж второго менеджера:\n"))
summa_prod3 = int(input("Введите сумму продаж третьего менеджера:\n"))

if summa_prod1 > 0 and summa_prod1 < 499:
    zp1 = summa_prod1 * 0.03 + 200
    print("зарплата первого менеджера:",summa_prod1+zp1)
elif summa_prod1 > 499 and summa_prod1 < 1000:
    zp1 = summa_prod1 * 0.05 + 200
    print("зарплата первого менеджера:",summa_prod1 + zp1)
elif summa_prod1 > 1000:
    zp1 = summa_prod1 * 0.08 + 200
    print("зарплата первого менеджера:",summa_prod1 + zp1)

if summa_prod2 > 0 and summa_prod2 < 499:
    zp2 = summa_prod2 * 0.03 + 200
    print("зарплата второго менеджера:",summa_prod2+zp2)
elif summa_prod2 > 499 and summa_prod2 < 1000:
    zp2 = summa_prod2 * 0.05 + 200
    print("зарплата второго менеджера:",summa_prod2 + zp2)
elif summa_prod2 > 1000:
    zp2 = summa_prod2 * 0.08 + 200
    print("зарплата второго менеджера:",summa_prod2 + zp2)

if summa_prod3 > 0 and summa_prod3 < 499:
    zp3 = summa_prod3 * 0.03 + 200
    print("зарплата третьего менеджера:",summa_prod3+zp3)
elif summa_prod3 > 499 and summa_prod3 < 1000:
    zp3 = summa_prod3 * 0.05 + 200
    print("зарплата третьего менеджера:",summa_prod3 + zp3)
elif summa_prod3 > 1000:
    zp3 = summa_prod3 * 0.08 + 200
    print("зарплата третьего менеджера:",summa_prod3 + zp3)

if zp1 > zp2 and zp1 >zp3:
   # zp1 + 200
    print("Первый менеджер продал больше всех и получает +200$ премии, итого:",summa_prod1 + zp1 + 200)
elif zp2 > zp1 and zp2 >zp3:
    print("Второй менеджер продал больше всех и получает +200$ премии, итого:", summa_prod2 + zp2+ 200)
elif zp3 > zp2 and zp3 > zp1:
    print("Третий менеджер продал больше всех и получает +200$ премии, итого:", summa_prod3 + zp3 + 200)