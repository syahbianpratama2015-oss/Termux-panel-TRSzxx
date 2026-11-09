import os
import time

def main():
    os.system("clear")
    print("=== 🎸 SETEL LAGU (DOWNLOAD DULU) ===")
    print("Ketik judul lagu (contoh: slank gara-gara rasta), atau 'keluar'.")
    print("Lagu bakal di-download ke folder ini, terus diputer.\n")
    
    while True:
        judul = input("Cari Lagu: ").strip()
        if judul.lower() == 'keluar': break
        if not judul: continue
        
        print(f"\n⏳ Mencari dan mengunduh '{judul}'...")
        print("(Tunggu bentar, ini ngambil file lagunya)")
        
        # Hapus file mp3 lama biar gak numpuk (opsional)
        os.system("rm -f *.mp3")
        
        # Download lagu pake yt-dlp
        cmd_download = f'yt-dlp "ytsearch1:{judul}" -x --audio-format mp3 -o "%(title)s.%(ext)s"'
        os.system(cmd_download)
        
        # Cari file mp3 terbaru
        try:
            files = [f for f in os.listdir('.') if f.endswith('.mp3')]
            if not files:
                print("❌ Gagal download lagu. Pastiin yt-dlp udah di-update.")
                continue
                
            files.sort(key=os.path.getmtime, reverse=True)
            lagu_baru = files[0]
            
            print(f"\n✅ Lagu berhasil di-download: {lagu_baru}")
            print("🎵 Memutar lagu...")
            
            # Panggil MPV Android
            os.system(f'mpv "{lagu_baru}"')
            
            print("💡 (Lagu diputar di MPV. Tutup MPV buat milih lagu lain)")
            time.sleep(1)
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
