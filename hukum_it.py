import os
import time

def main():
    os.system("clear")
    print("=== ⚖️ KAMUS HUKUM IT: LEGAL VS ILEGAL ===")
    print("Ketik aktivitas yang mau lu tanyain (misal: hack web, download lagu).")
    print("Ketik 'keluar' untuk berhenti.\n")
    
    while True:
        tanya = input("Tanya: ").lower().strip()
        if tanya == 'keluar': break
        if not tanya: continue
        
        print("\n⏳ Menganalisis...")
        time.sleep(1)
        os.system("clear")
        
        # Logika pengecekan
        if any(kata in tanya for kata in ["hack", "bobol", "sql", "xss"]):
            if "web sendiri" in tanya or "lab" in tanya or "belajar" in tanya:
                print("\033[1;32m✅ LEGAL (White Hat)\033[0m")
                print("Penjelasan: Ngetes keamanan web sendiri atau di lab simulasi itu legal dan dianjurkan untuk belajar.")
            else:
                print("\033[1;31m❌ ILEGAL (Black Hat)\033[0m")
                print("Penjelasan: Membobol sistem orang lain tanpa izin tertulis melanggar UU ITE Pasal 30.")
                print("Ancaman: Penjara maksimal 6-8 tahun dan/atau denda miliaran rupiah.")
                
        elif any(kata in tanya for kata in ["download", "bajakan", "crack", "torrent"]):
            print("\033[1;33m⚠️ ZONA ABU-ABU / ILEGAL\033[0m")
            print("Penjelasan: Mendownload konten berhak cipta tanpa izin (bajakan) melanggar UU Hak Cipta.")
            print("Ancaman: Denda dan penyitaan perangkat.")
            
        elif any(kata in tanya for kata in ["wifi", "hotspot", "scan", "nmap"]):
            if "sendiri" in tanya or "lab" in tanya or "milik" in tanya:
                print("\033[1;32m✅ LEGAL\033[0m")
                print("Penjelasan: Nge-scan jaringan sendiri atau hotspot sendiri itu legal.")
            else:
                print("\033[1;31m❌ ILEGAL\033[0m")
                print("Penjelasan: Nyadap atau nge-scan jaringan orang lain tanpa izin melanggar privasi (UU ITE Pasal 30 & 32).")
                
        elif any(kata in tanya for kata in ["phishing", "tipu", "scam", "palsu"]):
            print("\033[1;31m❌ ILEGAL (Pidana Berat)\033[0m")
            print("Penjelasan: Nipu orang pakai web palsu atau phishing itu penipuan online.")
            print("Ancaman: UU ITE Pasal 28 & 35, ancaman penjara 6-12 tahun.")
            
        elif any(kata in tanya for kata in ["ddos", "down", "serang"]):
            print("\033[1;31m❌ ILEGAL\033[0m")
            print("Penjelasan: Nyerang server orang sampai down (DDoS) itu tindak pidana siber.")
            print("Ancaman: UU ITE Pasal 30, penjara 6-10 tahun.")
            
        elif any(kata in tanya for kata in ["bikin apk", "coding", "belajar", "python"]):
            print("\033[1;32m✅ LEGAL 100%\033[0m")
            print("Penjelasan: Belajar ngoding dan bikin aplikasi sendiri itu legal dan bermanfaat.")
            
        else:
            print("\033[1;33m❓ TIDAK DIKETAHUI\033[0m")
            print("Penjelasan: Aktivitas belum terdaftar. Selama tidak merugikan orang lain dan tidak melanggar UU ITE, itu legal.")

if __name__ == "__main__":
    main()
