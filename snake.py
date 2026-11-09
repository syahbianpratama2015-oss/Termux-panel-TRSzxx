import os
import random
import time
import sys
import tty
import termios
import select

# Ukuran papan
BARIS = 15
KOLOM = 30
BLOK_KOSONG = "⬛"
KEPALA_ULAR = "🟩"
BADAN_ULAR = "🟢"
APEL = "🍎"

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

def gambar_papan(papan, skor, mode):
    clear()
    print(f"=== 🐍 ULAR JADUL ({mode.upper()}) ===")
    print(f"Skor (Apel): {skor} | Kontrol: W A S D | Q = Keluar")
    print("=" * 62)
    for row in papan:
        print("".join(row))
    print("=" * 62)

def main():
    clear()
    print("=== 🎮 PILIH MODE ULAR ===")
    print("1. Easy (Lambat)")
    print("2. Normal")
    print("3. Sedang")
    print("4. Sulit")
    print("5. Extreme")
    print("6. Nightmare")
    mode_pilih = input("\nPilih mode [1-6]: ")
    
    mode_dict = {
        '1': ("Easy", 0.3), '2': ("Normal", 0.2), '3': ("Sedang", 0.15),
        '4': ("Sulit", 0.1), '5': ("Extreme", 0.05), '6': ("Nightmare", 0.02)
    }
    mode_nama, delay = mode_dict.get(mode_pilih, ("Normal", 0.2))

    # Papan kosong
    papan = [[BLOK_KOSONG for _ in range(KOLOM)] for _ in range(BARIS)]
    
    # Ular awal (3 badan)
    ular = [[BARIS//2, KOLOM//2], [BARIS//2, KOLOM//2 - 1], [BARIS//2, KOLOM//2 - 2]]
    arah = 'd' # default ke kanan
    skor = 0
    
    # Apel pertama
    apel_r = random.randint(0, BARIS-1)
    apel_c = random.randint(0, KOLOM-1)
    while [apel_r, apel_c] in ular:
        apel_r = random.randint(0, BARIS-1)
        apel_c = random.randint(0, KOLOM-1)

    last_time = time.time()

    while True:
        # Gambar papan
        tampilan = [[BLOK_KOSONG for _ in range(KOLOM)] for _ in range(BARIS)]
        for i, (r, c) in enumerate(ular):
            if 0 <= r < BARIS and 0 <= c < KOLOM:
                tampilan[r][c] = KEPALA_ULAR if i == 0 else BADAN_ULAR
        tampilan[apel_r][apel_c] = APEL
        
        gambar_papan(tampilan, skor, mode_nama)
        
        # Auto gerak
        current_time = time.time()
        if (current_time - last_time) >= delay:
            # Geser badan
            new_head = [ular[0][0], ular[0][1]]
            if arah == 'w': new_head[0] -= 1
            elif arah == 's': new_head[0] += 1
            elif arah == 'a': new_head[1] -= 1
            elif arah == 'd': new_head[1] += 1

            # Cek nabrak dinding atau badan sendiri
            if (new_head[0] < 0 or new_head[0] >= BARIS or 
                new_head[1] < 0 or new_head[1] >= KOLOM or 
                new_head in ular):
                clear()
                print("\n" * 5)
                print("=" * 30)
                print(f"      SKOR LU: {skor} Apel")
                print("=" * 30)
                print("\n")
                print("      🗿  K A C U N G  🗿")
                print("\n")
                print("=" * 30)
                break

            # Cek makan apel
            if new_head == [apel_r, apel_c]:
                ular.insert(0, new_head)
                skor += 1
                # Bikin apel baru
                apel_r = random.randint(0, BARIS-1)
                apel_c = random.randint(0, KOLOM-1)
                while [apel_r, apel_c] in ular:
                    apel_r = random.randint(0, BARIS-1)
                    apel_c = random.randint(0, KOLOM-1)
            else:
                ular.insert(0, new_head)
                ular.pop()
            
            last_time = current_time

        # Input user
        cmd = get_key()
        if cmd == 'q': break
        elif cmd in ['w', 'W'] and arah != 's': arah = 'w'
        elif cmd in ['s', 'S'] and arah != 'w': arah = 's'
        elif cmd in ['a', 'A'] and arah != 'd': arah = 'a'
        elif cmd in ['d', 'D'] and arah != 'a': arah = 'd'

if __name__ == "__main__":
    main()
