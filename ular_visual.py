import random
pos = 0
while pos < 16:
    papan = ['⬜']*16
    papan[pos] = '🧑'
    if pos == 15: papan[pos] = '🏁'
    print("".join(papan[:4]))
    print("".join(papan[4:8]))
    print("".join(papan[8:12]))
    print("".join(papan[12:16]))
    input("Lempar dadu...")
    pos += random.randint(1, 6)
    if pos > 15: pos = 15
print("🏆 FINISH!")
