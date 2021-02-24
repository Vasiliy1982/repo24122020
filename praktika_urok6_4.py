#praktika_urok6_4
#Известно, что купит больше 5 единиц товара получит скидку 25%,
# а кто больше 10 единиц товара получит скидку 50%.
# Пользователь вводит цену единицы товара и сколько единиц хочет купить.
# Программа выводит итоговую цену с учётом полагающейся скидки. Цена округляются в меньшую сторону.
print("Введите цену товара")
price = int(input())
print("Введите количество товара которое желаете приобрести")
quantity = int(input())
summa = price*quantity
if quantity < 5:
    print("скидки нет")
if quantity >= 5 and quantity <=10:
    print("Скидка 25%")

    sale_price = summa * 25 / 100
    itog_price = (summa - sale_price)//1
    print(itog_price)
if quantity > 10:
    print("Скидка 50%")
    sale_price = summa * 50 / 100
    itog_price = (summa - sale_price) // 1
    print(itog_price)