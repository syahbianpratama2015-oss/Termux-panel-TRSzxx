import time
import os

HIJAU = '\033[1;32m'
CYAN = '\033[1;36m'
MERAH = '\033[1;31m'
RESET = '\033[0m'

os.system('clear')
os.system("timeout 3 cmatrix -s -C green")
os.system('clear')

def ketik(teks, kecepatan=0.05):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(kecepatan)
    print()

print("\n\n\n")
print(f"{MERAH}=================================================={RESET}")
ketik(f"{HIJAU}       SISTEM KEAMANAN TRSzxx BERHASIL DIAKTIFKAN...{RESET}", 0.04)
ketik(f"{HIJAU}       MEMBACA DATA BIOMETRIK... BERHASIL.{RESET}", 0.04)
time.sleep(0.5)
print(f"{MERAH}=================================================={RESET}")
ketik(f"{CYAN}          S E L A M A T   K E M B A L I ,   T U A N .{RESET}", 0.08)
print(f"{MERAH}=================================================={RESET}")
time.sleep(1)
