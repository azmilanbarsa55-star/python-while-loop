count = 0

while True:
    matn = input("Matn kiriting (to'xtatish uchun stop yozing): ")

    if matn == "stop":
        break

    count += 1

print("Siz", count, "marta matn kiritdingiz.")
