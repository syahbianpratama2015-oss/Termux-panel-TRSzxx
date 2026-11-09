# Daftar password yang sering dipakai orang (Kamus Hacker)
kamus_hacker = ["123456", "password", "admin", "qwerty", "bismillah", "sayang", "anjing"]

print("=== SIMULASI BRUTE-FORCE (DICTIONARY ATTACK) ===")
target = input("Masukkan password target (misal: admin): ")

ketemu = False

# Program bakal ngecek satu per satu dari kamus
for tebakan in kamus_hacker:
    print(f"Mencoba tebakan: {tebakan}...")
    
    if tebakan == target:
        print(f"\n💥 BOOM! Password berhasil dibobol: '{tebakan}'")
        ketemu = True
        break # Berhenti kalau udah ketemu
    else:
        print("❌ Gagal.\n")

if not ketemu:
    print("\n🛡️ Password aman! Nggak ada di kamus hacker.")
