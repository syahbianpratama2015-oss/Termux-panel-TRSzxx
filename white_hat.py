import time

def simulasi():
    print("="*40)
    print("🛡️ SIMULASI WHITE HAT: UJI KEAMANAN")
    print("="*40)
    print("Kamu adalah seorang White Hat Hacker.")
    print("Tugasmu: Ngetes celah keamanan sistem login.\n")
    
    time.sleep(1)
    
    # Sistem yang belum di-patch (Rentan)
    print("🔴 [FASE 1: SISTEM RENTAN]")
    print("Mencoba menembus sistem dengan SQL Injection...")
    time.sleep(1)
    
    user_input = "' OR 1=1 --"
    print(f"Mengirim payload: {user_input}")
    time.sleep(1)
    
    if "' OR 1=1 --" in user_input:
        print("🚨 AKSES DIBERIKAN! Sistem rentan SQL Injection!\n")
    else:
        print("❌ Akses ditolak.\n")
        
    time.sleep(2)
    
    # Sistem yang sudah di-patch (Aman)
    print("🟢 [FASE 2: SISTEM AMAN (SUDAH DI-PATCH)]")
    print("Kamu sebagai White Hat, menambal celah dengan 'Input Sanitization'...")
    time.sleep(1)
    print("Mencoba menembus sistem lagi...")
    time.sleep(1)
    
    # Simulasi filter (Satpam nangkep)
    if "'" in user_input or "--" in user_input:
        print("🛑 ALARM! Terdeteksi karakter mencurigakan (', --).")
        print("❌ AKSES DITOLAK! Sistem aman dari serangan.\n")
    else:
        print("Mencoba login normal...\n")
        
    time.sleep(1)
    print("="*40)
    print("✅ Simulasi Selesai.")
    print("Kamu berhasil menguji sistem dan menambal celahnya!")
    print("="*40)

# Jalanin fungsinya
simulasi()
