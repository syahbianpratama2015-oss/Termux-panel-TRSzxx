import hashlib
import time

target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
# (Hash ini didapat dari script server_target.py tadi)

print("=== TOOL: HASH CRACKER ===")
print("Memuat kamus...")

try:
    with open("kamus_hacker.txt", "r") as f:
        kata_kata = f.read().splitlines()
except:
    print("Bikin file kamus_hacker.txt dulu bang!")
    exit()

print(f"Mencoba {len(kata_kata)} tebakan...\n")
time.sleep(1)

for kata in kata_kata:
    hash_tebakan = hashlib.sha256(kata.encode()).hexdigest()
    
    if hash_tebakan == target_hash:
        print(f"💥 BOOM! Password Admin ditemukan: '{kata}'")
        print(f"Gunakan password ini untuk login ke server!")
        break
    else:
        print(f"[-] Mencoba '{kata}' -> Gagal")
