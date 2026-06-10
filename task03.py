ball = 0

while True:
    belgi = input("+ yoki stop yozing: ")

    if belgi == "+":
        ball += 10
        print("Ball:", ball)
    elif belgi == "stop":
        print("O'yin tugadi.")
        print("Umumiy ball:", ball)
        break
    else:
        print("Faqat + yoki stop yozing!")