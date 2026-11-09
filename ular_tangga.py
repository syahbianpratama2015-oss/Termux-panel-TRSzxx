import random
print("🎲 ULAR TANGGA TEKS")
pos = 0
while pos < 10:
    input("Enter untuk kocok dadu...")
    pos += random.randint(1, 6)
    print("Posisi:", pos)
print("🎉 MENANG!")
