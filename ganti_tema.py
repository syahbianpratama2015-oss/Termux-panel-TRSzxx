import os
import subprocess

print("=== 🎨 PENGATUR TEMA PANEL ===")
print("1. Tema Default (Hacker Cyan)")
print("2. Tema Cyberpunk (Ungu/Pink)")
print("3. Tema Hacker (Hijau Matrix)")
print("4. Tema Darah (Merah)")
print("5. Download Tema Baru (Update)")
print("0. Kembali")

pilih = input("\nPilih tema [0-5]: ")

if pilih == '1':
    warna = "CYAN='\\033[1;36m'; YELLOW='\\033[1;33m'; GREEN='\\033[1;32m'; RED='\\033[1;31m'"
elif pilih == '2':
    warna = "CYAN='\\033[1;35m'; YELLOW='\\033[1;36m'; GREEN='\\033[1;32m'; RED='\\033[1;31m'"
elif pilih == '3':
    warna = "CYAN='\\033[1;32m'; YELLOW='\\033[1;32m'; GREEN='\\033[1;32m'; RED='\\033[1;31m'"
elif pilih == '4':
    warna = "CYAN='\\033[1;31m'; YELLOW='\\033[1;33m'; GREEN='\\033[1;32m'; RED='\\033[1;31m'"
elif pilih == '5':
    print("\n⏳ Mengunduh paket tema baru dari server...")
    # Simulasi download tema baru
    os.system("sleep 2")
    print("✅ Tema 'Neon Blue' berhasil diunduh!")
    warna = "CYAN='\\033[1;34m'; YELLOW='\\033[1;36m'; GREEN='\\033[1;32m'; RED='\\033[1;31m'"
elif pilih == '0':
    exit()
else:
    print("❌ Pilihan tidak valid.")
    exit()

# Tulis tema ke file config
with open(os.path.expanduser("~/tema.conf"), "w") as f:
    f.write(warna + "\n")

print("\n✅ Tema berhasil dipasang!")
print("Silakan buka panel.sh lagi untuk melihat perubahannya.")
