import time, random
hp = 5
while hp > 0:
    print("HP Blok:", hp)
    input("Pukul (Enter)...")
    hp -= random.randint(1, 2)
print("💥 BLOK HANCUR!")
