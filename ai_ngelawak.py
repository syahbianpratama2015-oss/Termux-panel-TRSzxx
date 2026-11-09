import random
import time

# Database Lawakan
lawakan = [
    "Kenapa lampu lalu lintas warnanya merah, kuning, hijau? Ya kalau warnanya ungu, namanya lampu lalu lintas ungu dong.",
    "Percakapan saat wawancara kerja:\nHRD: 'Apa kelebihanmu?'\nPelamar: 'Saya jujur.'\nHRD: 'Contohnya?'\nPelamar: 'Sebenernya saya males kerja di sini.'",
    "Kenapa ayam menyeberang jalan? Karena di jalan raya ada zebra cross, bukan ayam cross.",
    "Kalo ada hacker nge-hack HP lu, jangan panik. Cukup tarik napas, bilang 'Woy', nanti dia balik lagi.",
    "Bapak: 'Nak, di sekolah dapat peringkat berapa?'\nAnak: 'Peringkat 3, Pak.'\nBapak: 'Hebat! Siapa yang nomor 1 dan 2?'\nAnak: 'Guru dan wali kelas, Pak.'",
    "Kenapa komputer gak pernah sakit gigi? Karena dia selalu pakai 'anti-virus'.",
    "Jangan bilang lu gak punya pacar, lu kan punya pacar kebersihan. Tiap hari nyapu."
]

# Database Pantun
pantun = [
    "Beli semangka di pasar malam,\nsambil jalan sambil makan.\nJangan suka menunda salam,\nnanti kena unfollow idaman.",
    "Bunga mawar bunga melati,\nditanam di depan istana.\nRajin-rajinlah belajar hari ini,\nbiar besok gak nyesel di masa tua.",
    "Ikan hiu makan tomat,\nmemang enak makan tomat.\nAku rindu berat,\ntapi kamu malah chat sama teman sekelas.",
    "Berlayar kapal ke Pulau Seribu,\nombak besar bikin mabuk.\nKalo kamu emang jodohku,\nkenapa malah nge-read doang gak dibales, bodoh."
]

# Database Tebak-tebakan
tebak_tebakan = [
    "Pertanyaan: Ayam apa yang bikin kesel?\nJawaban: Ayam-ayam aja yang ditanya, kok gue yang bingung.",
    "Pertanyaan: Bebek apa yang tingginya 100 meter?\nJawaban: Bebek yang lagi naik pesawat.",
    "Pertanyaan: Kenapa lampu depan mobil selalu putih?\nJawaban: Karena kalau item, namanya bukan lampu, tapi kacamata.",
    "Pertanyaan: Kalo lu jadi pohon, pohon apa?\nJawaban: Pohon yang selalu kangen sama kamu.",
    "Pertanyaan: Kue apa yang bikin mabuk?\nJawaban: Kue yang diterjunin dari lantai 10."
]

def ai_ngelawak():
    print("=== 🤖 AI NGELAWAK (OFFLINE MODE) ===")
    print("Ketik 'keluar' untuk berhenti.\n")
    
    while True:
        print("Lu: ", end="")
        user_input = input().lower()
        
        if user_input == 'keluar':
            print("AI: Yaudah, dadah! Tetap semangat, jangan lupa ketawa hari ini. 👋")
            break
            
        if "woi" in user_input or "lawak" in user_input or "halo" in user_input:
            print("\nAI: Woy! Siap-siap ketawa. Mau pilih apa nih?")
            print("1. Mau pantun? (Jenaka/Teka-teki/Seru-seruan)")
            print("2. Mau tebak-tebakan?")
            print("3. Mau aku sendiri yang ngelawak?\n")
            
            pilihan = input("Pilih [1-3]: ")
            
            print("\nAI: Mikir dulu ya...")
            time.sleep(1)
            
            if pilihan == '1':
                print(f"📜 PANTUN BUAT LU:\n\n{random.choice(pantun)}\n")
            elif pilihan == '2':
                print(f"❓ TEBAK-TEBAKAN:\n\n{random.choice(tebak_tebakan)}\n")
            elif pilihan == '3':
                print(f"😂 LAWAKAN DARI AI:\n\n{random.choice(lawakan)}\n")
            else:
                print("AI: Hah? Pilihan lu gak ada di menu bang. 😭\n")
        else:
            print("AI: Woy, ngomong yang jelas dong. Ketik 'woi ngelawak' biar gw mulai.\n")

if __name__ == "__main__":
    ai_ngelawak()
