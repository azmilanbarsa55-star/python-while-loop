b = True
while b:
    son = int(input("birinchi son: "))
    son2 = int(input("ikkinchi son: "))
    amal = input("amalni kiriting: ")
    if amal == "+":
        print(son + son2)
        a = input("yana davom etttirasizmi: ")
        if a == "yo'q":
            b = False
    elif amal == "-":
        print(son - son2)
        a = input("yana davom etttirasizmi: ")
        if a == "yo'q":
            b = False
    elif amal == "*":
        print(son * son2)
        a = input("yana davom etttirasizmi: ")
        if a == "yo'q":
            b = False
    elif amal == "/":
        print(son / son2)
        a = input("yana davom etttirasizmi: ")
        if a == "yo'q":
            b = False