import os
teks = input("Masukkan teks: ")
os.system(f"pkg install figlet -y > /dev/null; figlet {teks}")
