#DZ_Python_№4 задача3
число=int(input("Введите целое четырехзначное число"))
число1=число%10
число=число//10
число2=число%10
число=число//10
число3=число%10
число=число//10
число4=число%100
print(число1,число2,число3,число4)
