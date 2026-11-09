import os
kota = input("Nama Kota (misal: Jakarta): ")
os.system(f"curl -s 'https://api.aladhan.com/v1/timingsByCity?city={kota}&country=Indonesia&method=11' | grep -o '\"Fajr\":\"[^\"]*\"\|\"Dhuhr\":\"[^\"]*\"\|\"Asr\":\"[^\"]*\"\|\"Maghrib\":\"[^\"]*\"\|\"Isha\":\"[^\"]*\"'")
print("\n")
