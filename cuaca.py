import os
kota = input("Nama Kota (misal: Jakarta): ")
os.system(f"curl -s 'wttr.in/{kota}?format=3'")
