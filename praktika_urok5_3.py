# практическое задание3
диаметр = int(input("Введите диаметр:"))
площадь = (диаметр**2)/4*3.14
радиус = диаметр/2
периметр = 2*3.14*радиус
print("Если хотите получить значение площади, введите 1")
print("Если хотите получить значение периметра, введите 2")
выбор = input()
if выбор == "1":
    print(площадь)
if выбор == "2":
    print(периметр)
