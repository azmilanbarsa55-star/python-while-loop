import random

son = random.randint(1, 20)  # 1 dan 20 gacha tasodifiy son

while True:
    taxmin = int(input("1 dan 20 gacha son kiriting: "))

    if taxmin < son:
        print(f"men o'ylagan son {taxmin}dan katta")
    elif taxmin > son:
        print(f"men o'ylagan son {taxmin}dan kichik")
    else:
        print("Tabriklayman! Sonni topdingiz.")
        break