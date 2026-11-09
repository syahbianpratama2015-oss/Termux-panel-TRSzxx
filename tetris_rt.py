import os
import random
import time
import sys
import tty
import termios
import select

BARIS = 15
KOLOM = 10
BLOK_KOSONG = "⬛"
ANGKA_BLOK = ["2", "3", "4", "5", "6", "7", "8", "9"]

BENTUK = [
    [[1, 1, 1, 1]], [[1, 1], [1, 1]], [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]], [[0, 0, 1], [1, 1, 1]], [[0, 1, 1], [1, 1, 0]], [[1, 1, 0], [0, 1, 1]]
]

def clear(): os.system('clear')

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def gambar_papan(papan, blok_aktif, skor, warna_blok, mode):
    clear()
    print(f"=== 🧱 TETRIS RT ({mode.upper()}) ===")
    print(f"Skor: {skor} | Kontrol: W A S D, Spasi=Jatuh, Q=Keluar")
    print("=" * 22)
    tampilan = [row[:] for row in papan]
    if blok_aktif:
        r_pos, c_pos, bentuk = blok_aktif
        for r in range(len(bentuk)):
            for c in range(len(bentuk[r])):
                if bentuk[r][c] == 1:
                    if 0 <= r_pos + r < BARIS and 0 <= c_pos + c < KOLOM:
                        tampilan[r_pos + r][c_pos + c] = warna_blok
    for row in tampilan: print(" ".join(row))
    print("=" * 22)

def cek_bentrok(papan, bentuk, r_pos, c_pos):
    for r in range(len(bentuk)):
        for c in range(len(bentuk[r])):
            if bentuk[r][c] == 1:
                if r_pos + r >= BARIS or c_pos + c < 0 or c_pos + c >= KOLOM: return True
                if r_pos + r >= 0 and papan[r_pos + r][c_pos + c] != BLOK_KOSONG: return True
    return False

def putar_bentuk(bentuk):
    return [list(row) for row in zip(*bentuk[::-1])]

def main():
    clear()
    print("=== 🎮 PILIH MODE TETRIS RT ===")
    print("1. Easy (Sangat Mudah)")
    print("2. Normal")
    print("3. Sedang")
    print("4. Sulit")
    print("5. Extreme")
    print("6. Nightmare")
    mode_pilih = input("\nPilih mode [1-6]: ")
    
    mode_dict = {
        '1': ("Easy", 0), '2': ("Normal", 2), '3': ("Sedang", 1),
        '4': ("Sulit", 0.5), '5': ("Extreme", 0.2), '6': ("Nightmare", 0.05)
    }
    mode_nama, delay = mode_dict.get(mode_pilih, ("Normal", 2))

    papan = [[BLOK_KOSONG for _ in range(KOLOM)] for _ in range(BARIS)]
    skor = 0
    bentuk = random.choice(BENTUK)
    r_pos = 0
    c_pos = KOLOM // 2 - len(bentuk[0]) // 2
    warna_blok = random.choice(ANGKA_BLOK)
    last_time = time.time()

    while True:
        gambar_papan(papan, (r_pos, c_pos, bentuk), skor, warna_blok, mode_nama)
        
        current_time = time.time()
        if delay > 0 and (current_time - last_time) >= delay:
            if not cek_bentrok(papan, bentuk, r_pos + 1, c_pos):
                r_pos += 1
            last_time = current_time
        
        cmd = get_key()

        if cmd == 'q': break
        elif cmd in ['a', 'A']:
            if not cek_bentrok(papan, bentuk, r_pos, c_pos - 1): c_pos -= 1
        elif cmd in ['d', 'D']:
            if not cek_bentrok(papan, bentuk, r_pos, c_pos + 1): c_pos += 1
        elif cmd in ['s', 'S']:
            if not cek_bentrok(papan, bentuk, r_pos + 1, c_pos): r_pos += 1
        elif cmd in ['w', 'W']:
            bentuk_baru = putar_bentuk(bentuk)
            if not cek_bentrok(papan, bentuk_baru, r_pos, c_pos): bentuk = bentuk_baru
        elif cmd == ' ':
            while not cek_bentrok(papan, bentuk, r_pos + 1, c_pos): r_pos += 1
            
            for r in range(len(bentuk)):
                for c in range(len(bentuk[r])):
                    if bentuk[r][c] == 1:
                        papan[r_pos + r][c_pos + c] = warna_blok
            skor += 10
            
            for r in range(BARIS):
                if all(cell != BLOK_KOSONG for cell in papan[r]):
                    del papan[r]
                    papan.insert(0, [BLOK_KOSONG for _ in range(KOLOM)])
                    skor += 100
            
            bentuk = random.choice(BENTUK)
            r_pos = 0
            c_pos = KOLOM // 2 - len(bentuk[0]) // 2
            warna_blok = random.choice(ANGKA_BLOK)
            last_time = time.time()
            
            if cek_bentrok(papan, bentuk, r_pos, c_pos):
                clear()
                print("\n" * 5)
                print("=" * 22)
                print(f"         SKOR AKHIR LU: {skor}")
                print("=" * 22)
                print("\n")
                print("    🗿   K A C U N G   🗿")
                print("\n")
                print("=" * 22)
                break

if __name__ == "__main__":
    main()
