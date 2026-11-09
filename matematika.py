import os
def aljabar():
    print("\n=== 📐 ALJABAR ===")
    a = float(input("Nilai a: ")); b = float(input("Nilai b: ")); c = float(input("Nilai c: "))
    if a != 0: print(f"✅ Nilai x = {(c - b) / a}")
def kalkulus():
    print("\n=== 📈 KALKULUS ===")
    a = float(input("Koefisien a: ")); n = float(input("Pangkat n: "))
    if n == 0: print("✅ Turunan = 0")
    else: print(f"✅ Turunan f'(x) = {a * n}x^{n - 1}")
def dasar():
    print("\n=== ➕ MATEMATIKA DASAR ===")
    a = float(input("Angka 1: ")); b = float(input("Angka 2: "))
    print(f"Hasil Kali: {a * b}")
while True:
    os.system("clear")
    print("=====================================\n      📚 BELAJAR MATEMATIKA 📚\n=====================================")
    print("1. Dasar\n2. Aljabar\n3. Kalkulus\n0. Kembali")
    p = input("\nPilih [0-3]: ")
    if p == '1': dasar()
    elif p == '2': aljabar()
    elif p == '3': kalkulus()
    elif p == '0': break
    input("\nTekan [Enter]...")
