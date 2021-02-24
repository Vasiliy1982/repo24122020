#praktika_urok6_2
print("Введите число от 1 до 12 чтобы узнать к какому сезону он относится")
season = int(input())
if season > 0 and season <13:
    if season >=3 and season <= 5:
        print("Spring")
    if season >= 6 and season <= 8:
        print("Summer")
    if season >= 9 and season <= 9:
        print("Autumn")
    if season == 1 or season == 2 or season == 12:
        print("Winter")
else:
    print("В году двенадцать месяцев, от 1 до 12!")