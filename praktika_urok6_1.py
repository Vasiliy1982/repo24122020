#praktika_urok6_1
size_file_gig = int(input("Введите размер файла в гигабайтах"))
speed_inet = int(input("Введите скорость интернет соединения"))

size_file = size_file_gig*1024*1024*1024
upload_time = size_file/speed_inet

choice = input("Если хотите узнать время скачивания в часах введите: 1, если в минутах 2, в секундах 3")
if choice == "1":
    upload_time = upload_time//60//60
    print(upload_time)
if choice == "2":
    upload_time = upload_time // 60
    print(upload_time)
if choice == "3":
    upload_time = upload_time //1
    print(upload_time)
