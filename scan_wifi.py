import os
import subprocess

print("=== 🕵️‍♂️ SCANNER PENGGUNA WI-FI / HOTSPOT ===")
print("Fitur ini buat ngecek siapa aja yang nyambung ke jaringan lu.\n")

# Pastiin nmap terinstall
os.system("pkg install nmap -y > /dev/null 2>&1")

# Deteksi IP lokal HP lu
print("Mendeteksi IP HP lu...")
try:
    ip_hp = subprocess.check_output(["ifconfig", "wlan0"], text=True)
    for line in ip_hp.splitlines():
        if "inet " in line:
            ip_lokal = line.split("inet ")[1].split(" ")[0]
            print(f"✅ IP HP Lu: {ip_lokal}")
            break
    else:
        print("❌ Gagal dapet IP. Pastiin Wi-Fi/Hotspot nyala!")
        exit()
except Exception:
    print("❌ Gagal baca jaringan. Pastiin lu lagi nyambung ke Wi-Fi/Hotspot.")
    exit()

# Ngambil IP Network (misal 192.168.1.5 jadi 192.168.1.0/24)
ip_network = ".".join(ip_lokal.split(".")[:-1]) + ".0/24"
print(f"\n🔍 Nge-scan jaringan: {ip_network}")
print("Tunggu sebentar ya, ini bisa makan waktu 10-30 detik...\n")

# Jalanin nmap (Ping scan aja biar cepet)
os.system(f"nmap -sn {ip_network}")

print("\n✅ Scan Selesai! Itu daftar HP/laptop yang nyambung ke jaringan lu.")
print("💡 Catatan: Kalau nama perangkatnya 'Unknown', berarti perangkat itu nyembunyiin nama.")
