def cek_kekuatan_password(password):
    skor = 0
    alasan = []

    # 1. Cek Panjang Password
    if len(password) >= 8:
        skor += 1
    else:
        alasan.append("- Terlalu pendek (minimal 8 karakter)")

    # 2. Cek Huruf Besar (A-Z)
    if any(huruf.isupper() for huruf in password):
        skor += 1
    else:
        alasan.append("- Gak ada huruf besar (A-Z)")

    # 3. Cek Huruf Kecil (a-z)
    if any(huruf.islower() for huruf in password):
        skor += 1
    else:
        alasan.append("- Gak ada huruf kecil (a-z)")

    # 4. Cek Angka (0-9)
    if any(huruf.isdigit() for huruf in password):
        skor += 1
    else:
        alasan.append("- Gak ada angka (0-9)")

    # 5. Cek Simbol (seperti @, #, $, !, dll)
    if any(not huruf.isalnum() for huruf in password):
        skor += 1
    else:
        alasan.append("- Gak ada simbol unik (@, #, $, !, dll)")

    # --- Hasil Akhir ---
    print("\n=== HASIL ANALISIS ===")
    if skor == 5:
        print("✅ SANGAT KUAT! Hacker bakal nangis liat password ini.")
    elif skor == 4:
        print("🟡 KUAT, tapi masih bisa ditingkatkan.")
    elif skor == 3:
        print("🟠 SEDANG. Lumayan, tapi gampang ditebak.")
    else:
        print("🚨 LEMAH BANGET! Gampang dibobol pakai brute-force.")

    if alasan:
        print("\nSaran Perbaikan:")
        for a in alasan:
            print(a)
    print("-" * 30)

# --- PROGRAM UTAMA ---
print("=== SISTEM KEAMANAN PASSWORD ===")
while True:
    print("\nKetik 'keluar' untuk berhenti.")
    pw = input("Masukkan password yang mau dites: ")
    
    if pw.lower() == 'keluar':
        print("Program berhenti. Jaga selalu keamananmu! 🛡️")
        break
        
    cek_kekuatan_password(pw)
