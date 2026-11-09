import os

def api_offline():
    print("\n=== 🤖 API OFFLINE ===")
    print("Ketik 'keluar' untuk kembali.")
    while True:
        tanya = input("\nLu: ").lower()
        if tanya == 'keluar': break
        elif "python" in tanya: print("AI: Python itu bahasa masa depan!")
        elif "hacker" in tanya: print("AI: Hacker sejati itu White Hat!")
        elif "api" in tanya: print("AI: Ini adalah API lokal, jalan tanpa internet.")
        else: print("AI: Maaf, database offline saya terbatas.")

def enkripsi():
    print("\n=== 🔐 SIMULASI ENKRIPSI (CAESAR) ===")
    teks = input("Masukkan teks: ")
    kunci = int(input("Geser berapa langkah (1-25): "))
    hasil = ""
    for h in teks:
        if h.isalpha():
            batas = ord('A') if h.isupper() else ord('a')
            hasil += chr((ord(h) - batas + kunci) % 26 + batas)
        else: hasil += h
    print(f"Hasil Enkripsi: {hasil}")

def spek_hp():
    print("\n=== 📱 INFO HP ===")
    print("Merk:", os.popen("getprop ro.product.brand").read().strip())
    print("Model:", os.popen("getprop ro.product.model").read().strip())
    print("Android:", os.popen("getprop ro.build.version.release").read().strip())
    print("Arsitektur:", os.popen("uname -m").read().strip())

def matriks():
    print("\n=== 🧮 KALKULATOR MATRIKS 2x2 ===")
    print("Matriks: [ a b ]")
    print("          [ c d ]")
    a = float(input("Nilai a: "))
    b = float(input("Nilai b: "))
    c = float(input("Nilai c: "))
    d = float(input("Nilai d: "))
    det = (a * d) - (b * c)
    print(f"Determinan (ad - bc) = {det}")

def angka_hoki():
    print("\n=== 🍀 PELACAK ANGKA HOKI ===")
    nama = input("Masukkan nama lu: ")
    total = sum(ord(c) for c in nama)
    hoki = (total * 7) % 100
    print(f"Angka hoki lu hari ini: {hoki}")

while True:
    os.system("clear")
    print("=====================================")
    print("         T O O L S   T R S z x x     ")
    print("=====================================")
    print("1. API Offline (Chatbot)")
    print("2. Simulasi Enkripsi Pesan")
    print("3. Info Spesifikasi HP")
    print("4. Kalkulator Matriks 2x2")
    print("5. Pelacak Angka Hoki")
    print("0. Kembali ke Panel Utama")
    
    pilih = input("\nPilih menu [0-5]: ")
    if pilih == '1': api_offline()
    elif pilih == '2': enkripsi()
    elif pilih == '3': spek_hp()
    elif pilih == '4': matriks()
    elif pilih == '5': angka_hoki()
    elif pilih == '0': break
    else: print("Pilihan salah!")
    input("\nTekan [Enter] untuk lanjut...")
