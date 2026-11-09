import hashlib
import time

print("=== SIMULASI DICTIONARY ATTACK ===")

# 1. Minta input target hash (Kita pakai hash SHA-256 dari kata "kucing")
# Hash ini ibarat "Password yang udah dikunci di database".
target_hash = input("Masukkan Target Hash: ")

# Kalau lu males ngetik hash panjang, lu bisa langsung pencet Enter
if target_hash == "":
    target_hash = "d1d6c5e6f1f9d6e2a3fbf1e2b8e4c9e7d5f4f1e5e6e7e8e9a0b1c2d3e4f5a6b7" 
    # (Anggap aja ini hash dari kata "kucing", biar simpel)

# 2. Buka file kamus.txt
try:
    with open("kamus.txt", "r") as file_kamus:
        daftar_kata = file_kamus.read().splitlines()
except FileNotFoundError:
    print("❌ Error: File 'kamus.txt' gak ketemu! Bikin dulu sana.")
    exit()

print(f"\n[+] Memuat {len(daftar_kata)} kata dari kamus...")
print(f"[+] Target Hash: {target_hash}")
print("[+] Mulai menyerang...\n")

# 3. Proses nembak (Brute-force pakai kamus)
waktu_mulai = time.time()
ketemu = False

for kata in daftar_kata:
    # Ubah kata jadi hash
    hash_tebakan = hashlib.sha256(kata.encode()).hexdigest()
    
    # Cocokin
    if hash_tebakan == target_hash:
        waktu_selesai = time.time()
        total_waktu = waktu_selesai - waktu_mulai
        
        print(f"💥 BOOM! TARGET BERHASIL DIBOBOL!")
        print(f"🔑 Password asli: '{kata}'")
        print(f"⏱️ Waktu yang dibutuhkan: {total_waktu:.4f} detik")
        ketemu = True
        break
    else:
        print(f"[-] Mencoba '{kata}' -> Gagal")

if not ketemu:
    print("\n❌ Gagal! Password gak ada di kamus. Sistem ini cukup aman.")
