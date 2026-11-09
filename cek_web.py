import os
url = input("Masukkan URL (contoh: google.com): ")
if not url.startswith("http"): url = "https://" + url
print(f"\n🔍 Ngecek status {url}...")
os.system(f"curl -s -o /dev/null -w 'Status Code: %{{http_code}}\nWaktu Respon: %{{time_total}} detik\n' {url}")
