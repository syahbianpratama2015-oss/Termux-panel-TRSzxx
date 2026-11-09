import hashlib
pw = input("Masukkan password yang mau dites: ")
if len(pw) < 8: print("🚨 LEMAH! Minimal 8 karakter.")
elif pw.isdigit(): print("🚨 LEMAH! Jangan cuma angka.")
else: print("✅ KUAT! Password lu aman.")
