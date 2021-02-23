# DZ_Python_№5_2
metrs = int(input("Введите некоторое количество метров:"))

mili = metrs * 0.000621371
inch = metrs * 0.0254
yard = metrs * 0.9144

print("Если хотите перевести метры в мили введите 1, если в дюймы 2 в ярды 3")

choice = input()
if choice == "1":
    print(mili)
if choice == "2":
    print(inch)
if choice == "3":
    print(yard)