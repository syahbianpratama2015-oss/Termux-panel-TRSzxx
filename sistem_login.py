import hashlib

# Ini hash yang lu curi dari database perusahaan
target_hash = "21232f297a57a5a743894a0e4a801fc3" # Punya Budi

# Kamus kata yang mau lu coba
kamus_kata = ["123456", "password", "rahasia123", "admin", "budi", "sayang"]

print(f"Target Hash: {target_hash}")
print("Mulai mencocokkan dengan kamus...\n")

ketemu = False
for kata in kamus_kata:
    # Ubah kata di kamus jadi hash
    hash_tebakan = hashlib.sha256(kata.encode()).hexdigest()
    
    # Cocokin sama target
    if hash_tebakan == target_hash:
        print(f"💥 BOOM! Hash berhasil dipecahkan!")
        print(f"Password asli Budi adalah: '{kata}'")
        ketemu = True
        break
    else:
        print(f"Coba '{kata}' -> Gagal.")

if not ketemu:
    print("Password tidak ada di kamus. Butuh waktu lama untuk pecahin.")
