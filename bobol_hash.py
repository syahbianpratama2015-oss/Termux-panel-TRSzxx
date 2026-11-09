import hashlib

# Hash SHA-256 dari kata "admin"
target_hash = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
kamus_kata = ["123456", "password", "rahasia123", "admin", "budi", "sayang"]

print("Target Hash:", target_hash)
print("Mulai mencocokkan dengan kamus...\n")

ketemu = False
for kata in kamus_kata:
    hash_tebakan = hashlib.sha256(kata.encode()).hexdigest()
    
    if hash_tebakan == target_hash:
        print(f"💥 BOOM! Hash berhasil dipecahkan!")
        print(f"Password asli adalah: '{kata}'")
        ketemu = True
        break
    else:
        print(f"Coba '{kata}' -> Gagal.")
