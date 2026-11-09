import hashlib

print("=====================================")
print("   SERVER UTAMA PT. MAJU BERSAMA     ")
print("=====================================")
print("Menginisialisasi database...")

# Database rahasia (Password belum diketahui hacker)
# Admin = super123
# Direktur = rahasia2023
database = {
    "admin": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", 
    "direktur": "d1d6c5e6f1f9d6e2a3fbf1e2b8e4c9e7d5f4f1e5e6e7e8e9a0b1c2d3e4f5a6b7"
}

# Hacker cuma punya akses ke hash ini
target_hash = database["admin"] 

print("\n[SYSTEM] File database berhasil dicuri!")
print(f"[SYSTEM] Hash target (Admin): {target_hash}")
print("\n[SYSTEM] Menunggu serangan...")

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Sistem login
while True:
    print("\n-------------------------------------")
    print("Silakan login (ketik 'exit' untuk keluar)")
    user = input("Username: ")
    if user == "exit": break
    
    pw = input("Password: ")
    
    if user in database:
        if hash_pass(pw) == database[user]:
            print(f"\n✅ AKSES DITERIMA! Selamat datang, {user}.")
            print("🔓 FLAG RAHASIA: NASI_PADANG_ENAK_BANGET")
            break
        else:
            print("\n❌ AKSES DITOLAK! Password salah.")
    else:
        print("\n❌ AKSES DITOLAK! User tidak ditemukan.")
