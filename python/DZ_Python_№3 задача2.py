#DZ_Python_№3 задача2

минуты=int(input("Введите время в минутах, которое хотите перевести в часы:"))
часы=минуты//60
остаток_минут=минуты%60
print(часы,"ч."," ",остаток_минут,"мин.")