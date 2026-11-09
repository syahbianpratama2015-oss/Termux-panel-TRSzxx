import os
import time
import random

# Database pantun AI
pantun_db = [
    {
        "soal": "Beli semangka di pasar malam,\nsambil jalan sambil makan.\nJangan suka menunda salam,\nnanti kena...",
        "jawaban": ["unfollow", "unfollow idaman", "unfollow teman"],
        "hint": "Awas kena ini kalau gak salam!"
    },
    {
        "soal": "Ikan hiu makan tomat,\nmemang enak makan tomat.\nAku rindu berat,\ntapi kamu malah chat sama...",
        "jawaban": ["teman sekelas", "teman", "mantan"],
        "hint": "Orang yang bikin lu cemburu"
    },
    {
        "soal": "Bunga mawar bunga melati,\nditanam di depan istana.\nRajin-rajinlah belajar hari ini,\nbiar besok gak nyesel di...",
        "jawaban": ["masa tua", "masa depan", "kemudian"],
        "hint": "Sesuatu yang terjadi nanti"
    }
]

# Pantun balasan AI (kalau lu nantangin dia)
pantun_balasan = [
    "Ke pasar beli pepaya,\npulangnya mampir ke warung.\nKamu nantangin saya,\ntapi saya tetap tersenyum.",
    "Bunga mawar berwarna merah,\nditanam di taman yang indah.\nKamu bikin pantun gak jelas,\ntapi saya tetap semangat belajar.",
    "Ada semut di atas meja,\nsemut kecil berwarna hitam.\nKamu pintar bikin pantun,\ntapi saya juga gak mau kalah.",
    "Pergi ke pantai bawa kamera,\nambil foto sama keluarga.\nTerima kasih pantunnya,\nsemoga kita tetap bersahabat selamanya."
]

def mode_ai_nantang():
    os.system("clear")
    print("=== 🎭 MODE 1: AI NANTANGIN LU ===")
    print("Lengkapi pantun di bawah ini!\n")
    
    soal = random.choice(pantun_db)
    print(soal['soal'])
    print(f"💡 Hint: {soal['hint']}")
    
    jawaban_user = input("\nJawaban lu: ").lower().strip()
    if jawaban_user in soal['jawaban']:
        print("\n✅ BENAR! Pinter banget.")
    else:
        print(f"\n❌ SALAH! Jawaban yang bener: {soal['jawaban'][0]}")

def mode_lu_nantang():
    os.system("clear")
    print("=== 🎭 MODE 2: LU NANTANGIN AI ===")
    print("Ketik pantun buatan lu, nanti AI bakal jawab pakai pantun juga!\n")
    
    pantun_lu = input("Pantun Lu: ")
    if not pantun_lu.strip(): return
    
    print("\n⏳ AI lagi mikir...")
    time.sleep(1.5)
    os.system("clear")
    
    print("=== PANTUN LU ===")
    print(pantun_lu)
    print("\n=== PANTUN BALASAN AI ===")
    print(random.choice(pantun_balasan))

def mode_bikin_pantun():
    os.system("clear")
    print("=== 🎭 MODE 3: BIKIN PANTUN BERSAMA ===")
    topik = input("Mau topik apa? (misal: cinta, hujan, kopi): ")
    if not topik.strip(): return
    
    print(f"\n⏳ AI lagi ngerangkai pantun tentang '{topik}'...")
    time.sleep(1.5)
    os.system("clear")
    
    print(f"=== PANTUN TENTANG {topik.upper()} ===")
    print(f"Pergi ke pasar beli {topik},")
    print("Jangan lupa bawa keranjang.")
    print(f"Kalau kamu memang suka {topik},")
    print("Jangan lupa jangan baperan.")
    
def main():
    while True:
        os.system("clear")
        print("=== 🎭 GAME PANTUN INTERAKTIF ===")
        print("1. AI Nantangin Lu (Lengkapi Pantun)")
        print("2. Lu Nantangin AI (Bikin Pantun Balasan)")
        print("3. AI Bikin Pantun (Topik Bebas)")
        print("0. Kembali")
        
        pilih = input("\nPilih [0-3]: ")
        if pilih == '1': mode_ai_nantang()
        elif pilih == '2': mode_lu_nantang()
        elif pilih == '3': mode_bikin_pantun()
        elif pilih == '0': break
        else: print("Pilihan salah!")
        input("\nTekan [Enter] untuk lanjut...")

if __name__ == "__main__":
    main()
