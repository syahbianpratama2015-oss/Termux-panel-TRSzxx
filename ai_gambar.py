import os
import time
import json
import datetime
import random

FILE_DB = os.path.expanduser("~/api_vip_db.json")
MASTER_KEY = "TRZ-MASTER-UNLIMITED"

def load_db():
    if os.path.exists(FILE_DB):
        with open(FILE_DB, 'r') as f:
            return json.load(f)
    return {}

def simpan_db(data):
    with open(FILE_DB, 'w') as f:
        json.dump(data, f)

gambar_db = {
    "kucing": """
       /\\_/\\
      (o.o)  <- MEOW
      ( > < )
    """,
    "kurama": """
       /\\   /\\
      ( o.o )  <- KUYANG!
       > ^ <
      /  |  \\
     /   |   \\
        _|_ _|_
       (_____)__
    """,
    "rumah": """
         /\\
        /  \\
       /____\\
       |    |
       | 10 |
       |____|
    """,
    "bebek": """
        __
      <(o )___
       ( ._> /
        `---'
    """,
    "robot": """
       [###]
       |o o|
       |_-_|
      /|   |\\
       |___|
    """
}

teks_3d = {
    "A": [" 010 ", "01 10", "01010", "01 10", "01 10"],
    "B": ["0100 ", "01 01", "0100 ", "01 01", "0100 "],
    "C": [" 0101", "01   ", "01   ", "01   ", " 0101"],
    "D": ["0100 ", "01 01", "01 01", "01 01", "0100 "],
    "E": ["01010", "01   ", "0100 ", "01   ", "01010"],
    "F": ["01010", "01   ", "0100 ", "01   ", "01   "],
    "G": [" 0101", "01   ", "01 01", "01 01", " 0100"],
    "H": ["01 01", "01 01", "01010", "01 01", "01 01"],
    "I": ["01010", " 010 ", " 010 ", " 010 ", "01010"],
    "J": ["  010", "  010", "  010", "01 10", " 010 "],
    "K": ["01 01", "01 10", "0100 ", "01 10", "01 01"],
    "L": ["01   ", "01   ", "01   ", "01   ", "01010"],
    "M": ["01 01", "01010", "01 01", "01 01", "01 01"],
    "N": ["01 01", "01101", "01 01", "01 01", "01 01"],
    "O": [" 010 ", "01 10", "01 10", "01 10", " 010 "],
    "P": ["0100 ", "01 01", "0100 ", "01   ", "01   "],
    "Q": [" 010 ", "01 10", "01 10", "01 10", " 0101"],
    "R": ["0100 ", "01 01", "0100 ", "01 10", "01 01"],
    "S": [" 0101", "01   ", " 010 ", "  010", "0101 "],
    "T": ["01010", " 010 ", " 010 ", " 010 ", " 010 "],
    "U": ["01 01", "01 01", "01 01", "01 01", " 010 "],
    "V": ["01 01", "01 01", "01 01", " 010 ", " 010 "],
    "W": ["01 01", "01 01", "01 01", "01010", "01 01"],
    "X": ["01 01", "01 01", " 010 ", "01 01", "01 01"],
    "Y": ["01 01", "01 01", " 010 ", " 010 ", " 010 "],
    "Z": ["01010", "  010", " 010 ", "010  ", "01010"],
    " ": ["   ", "   ", "   ", "   ", "   "]
}

def gambar_teks(kata):
    kata = kata.upper()
    hasil = ""
    for i in range(5):
        baris = ""
        for huruf in kata:
            if huruf in teks_3d:
                baris += teks_3d[huruf][i] + "  "
            else:
                baris += "????  "
        hasil += baris + "\n"
    return hasil

def ai_ngobrol(perintah):
    # Logika obrolan santai
    if "halo" in perintah or "hai" in perintah or "woi" in perintah:
        return random.choice(["Halo juga Tuan! 👋", "Woi! Ada yang bisa gw bantu? 😎", "Hai Tuan, siap ngoding lagi?"])
    elif "kabar" in perintah or "apa kabar" in perintah:
        return "Kabar baik dong Tuan! Sistem berjalan normal. 🟢"
    elif "siapa lu" in perintah or "siapa kamu" in perintah:
        return "Gw AI lokal buatan Tuan TRSzxx. Gw tinggal di dalam Termux. 🤖"
    elif "lagi apa" in perintah:
        return "Lagi nungguin perintah dari Tuan nih. 😴"
    elif "capek" in perintah:
        return "Capek? Istirahat dulu Tuan. Jangan lupa minum air putih. 🥤"
    elif "sayang" in perintah or "cinta" in perintah:
        return "Eaaakk... Tuan lagi galau ya? Wkwk. ❤️"
    elif "terima kasih" in perintah or "makasih" in perintah:
        return "Sama-sama Tuan! Senang bisa membantu. 🙏"
    elif "gmn" in perintah or "gimana" in perintah:
        return "Caranya gampang Tuan, tinggal dipelajari aja. 😎"
    else:
        return None # Kalau gak ada di database obrolan, lanjut ke gambar

def main():
    os.system("clear")
    print("=== 🎨 AI GABUNGAN (GAMBAR & NGOBROL) ===")
    
    kunci = input("Masukkan API Key VIP lu: ")
    db = load_db()
    hari_ini = datetime.date.today()
    
    if kunci == MASTER_KEY:
        print("\n✅ AKSES ADMIN DITERIMA! (UNLIMITED) 👑")
    elif kunci in db:
        tgl_exp = datetime.datetime.strptime(db[kunci]['kadaluarsa'], "%Y-%m-%d").date()
        if hari_ini > tgl_exp:
            print(f"\n🚨 API KEY EXPIRED! Silakan beli baru. 💸")
            return
        elif db[kunci]['kuota'] > 0:
            db[kunci]['kuota'] -= 1
            simpan_db(db)
            print(f"\n✅ AKSES VIP DITERIMA! (Sisa kuota: {db[kunci]['kuota']}) 🎟️")
        else:
            print("\n🚨 KUOTA HABIS! Silakan isi ulang. 💸")
            return
    else:
        print("\n❌ API KEY INVALID! AKSES DITOLAK. 🚫")
        return

    time.sleep(1)
    os.system("clear")
    
    print("🤖 AI siap ngobrol atau ngegambar!")
    print("Ketik 'keluar' untuk berhenti.\n")
    
    while True:
        perintah = input("Lu: ").lower().strip()
        if perintah == 'keluar': break
        if not perintah: continue
        
        print("\nAI: Mikir... 🤔")
        time.sleep(1)
        
        # 1. Cek Obrolan Dulu
        jawaban_obrolan = ai_ngobrol(perintah)
        if jawaban_obrolan:
            print(f"AI: {jawaban_obrolan}\n")
            continue
            
        # 2. Cek Gambar Database
        match = False
        for kata_kunci, ascii_gambar in gambar_db.items():
            if kata_kunci in perintah:
                print(f"=== GAMBAR {kata_kunci.upper()} ===")
                print(ascii_gambar)
                match = True
                break
                
        # 3. Kalau bukan obrolan atau gambar database, jadikan Teks 3D
        if not match:
            print("=== TEKS 3D ANGKA ===")
            print(gambar_teks(perintah))
            print("=====================\n")

if __name__ == "__main__":
    main()
