import os
import random
import string
import json
import datetime
import time

FILE_DB = os.path.expanduser("~/api_vip_db.json")
PASSWORD_UTAMA = "TRZ-RAHASIA"

def load_db():
    if os.path.exists(FILE_DB):
        with open(FILE_DB, 'r') as f:
            return json.load(f)
    return {}

def save_db(data):
    with open(FILE_DB, 'w') as f:
        json.dump(data, f)

def buat_key():
    acak = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"VIP-{acak}"

def kuis():
    os.system("clear")
    print("=== 🧠 KUIS DAPET API KEY GRATIS (30 HARI) ===")
    print("Jawab 3 pertanyaan receh ini dengan benar buat dapet akses VIP!\n")
    
    # Jawaban udah dihapus dari soal, biar lu mikir beneran 😎
    soal = [
        {"tanya": "Hacker yang nge-hack sistem buat ngetes keamanan, tapi gak ngambil data, disebut hacker apa? (2 kata)", "jawab": ["white hat", "whitehat"]},
        {"tanya": "Aplikasi terminal hitam yang lagi lu pake sekarang namanya apa?", "jawab": ["termux"]},
        {"tanya": "Apa nama bahasa pemrograman yang identik sama ular?", "jawab": ["python"]}
    ]
    
    skor = 0
    for i, s in enumerate(soal, 1):
        print(f"Soal {i}: {s['tanya']}")
        jawaban_user = input("Jawaban lu: ").lower().strip()
        
        if jawaban_user in s['jawab']:
            print("✅ BENAR!\n")
            skor += 1
        else:
            print(f"❌ SALAH!\n") # Jawaban benernya gak ditampilin
        time.sleep(0.5)
        
    if skor == 3:
        print("🎉 SELAMAT! Lu dapet API Key VIP Gratis!")
        kunci = buat_key()
        hari_ini = datetime.date.today()
        kadaluarsa = hari_ini + datetime.timedelta(days=30)
        
        db = load_db()
        db[kunci] = {
            "nama": "Pemenang Kuis", 
            "kuota": 5, 
            "dibuat": str(hari_ini), 
            "kadaluarsa": str(kadaluarsa)
        }
        save_db(db)
        
        print(f"\n🔑 Kunci Lu: {kunci}")
        print(f"🎟️ Kuota: 5 kali")
        print(f"📅 Berlaku Sampai: {kadaluarsa}")
        print("Gunakan kunci ini di Menu 61 (AI VIP).")
    else:
        print(f"❌ Maaf, skor lu {skor}/3. Lu harus jawab bener semua buat dapet API Key!")
        print("Coba lagi lain kali.")

def main():
    os.system("clear")
    print("=== 🔒 AKSES KUIS VIP ===")
    pw = input("Masukkan Password Utama: ")
    
    if pw == PASSWORD_UTAMA:
        print("\n✅ PASSWORD BENAR! Silakan jawab kuisnya.\n")
        time.sleep(1)
        kuis()
    else:
        print("\n❌ PASSWORD SALAH! AKSES DITOLAK. 🚫")
        print("Silakan coba lagi nanti.")
        time.sleep(2)

if __name__ == "__main__":
    main()
