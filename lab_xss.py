pesan = input("Masukkan script: ")
if "<script>" in pesan: print("💥 BOOM! Rentan XSS!")
else: print("✅ Aman.")
