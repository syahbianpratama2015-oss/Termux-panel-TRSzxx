import os
os.system("pkg install nmap -y > /dev/null")
ip = input("Masukkan IP (misal 8.8.8.8): ")
os.system(f"nmap {ip}")
