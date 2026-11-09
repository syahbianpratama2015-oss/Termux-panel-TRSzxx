import os

# Daftar kata yang dilarang (bisa lu tambahin sendiri)
kata_kasar = ["anjing", "bangsat", "monyet", "kontol", "memek", "tai", "babi", "tolol", "goblok"]

def sensor(teks):
    teks_lower = teks.lower()
    for kata in kata_kasar:
        # Ganti kata kasar pakai bintang
        teks_lower = teks_lower.replace(kata, kata[0] + "*" * (len(kata) - 2) + kata[-1])
    return teks_lower.capitalize()

print("=== 🚫 DETEKTOR KATA KASAR ===")
print("Ketik 'keluar' untuk berhenti.\n")

while True:
    kalimat = input("Lu: ")
    if kalimat.lower() == 'keluar': break
    
    hasil = sensor(kalimat)
    print(f"Sistem: {hasil}\n")
