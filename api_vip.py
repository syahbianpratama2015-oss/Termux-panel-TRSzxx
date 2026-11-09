import os
import random
import string
import json
import datetime

FILE_DB = os.path.expanduser("~/api_vip_db.json")
PASSWORD_UTAMA = "TRZ-RAHASIA" # PASSWORD UTAMA BUAT BIKIN API KEY

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

def main():
    os.system("clear")
    print("=== 🔑 API KEY (AI) VIP GENERATOR ===")
    print("Fitur ini membutuhkan Password Utama.\n")
    
    pw = input("Masukkan Password Utama: ")
    if pw != PASSWORD_UTAMA:
        print("\n❌ PASSWORD SALAH! AKSES DITOLAK. 🚫")
        print("💡 (Kalau lupa password, coba ke Menu 62 aja buat dapet API gratis lewat kuis)")
        return

    print("\n✅ PASSWORD BENAR! Selamat datang Admin. 👑")
    nama = input("Nama Pemilik API Key: ")
    try:
        kuota = int(input("Mau kasih kuota berapa kali pakai? (misal 10): "))
    except:
        print("❌ Kuota harus angka!")
        return
    
    # Logika 30 hari
    hari_ini = datetime.date.today()
    kadaluarsa = hari_ini + datetime.timedelta(days=30)
    
    kunci = buat_key()
    db = load_db()
    db[kunci] = {
        "nama": nama, 
        "kuota": kuota, 
        "dibuat": str(hari_ini), 
        "kadaluarsa": str(kadaluarsa)
    }
    save_db(db)
    
    print(f"\n✅ API KEY VIP BERHASIL DIBUAT!")
    print(f"🔑 Kunci: {kunci}")
    print(f"👤 Pemilik: {nama}")
    print(f"🎟️ Kuota: {kuota} kali")
    print(f"📅 Berlaku Sampai: {kadaluarsa}")
    print("Silakan gunakan kunci ini untuk masuk ke Menu 61 (AI VIP).")

if __name__ == "__main__":
    main()
