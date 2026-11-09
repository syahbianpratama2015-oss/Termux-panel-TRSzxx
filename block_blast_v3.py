import os
import random
import sys
import tty
import termios
import select

BARIS = 8
KOLOM = 8
KOSONG = "⬛"
WARNA = ["🟥", "🟦", "🟩", "🟨", "🟪"]
KURSOR_WARNA = "🔲"

BENTUK = [
    [[1]], [[1, 1]], [[1], [1]], [[1, 1], [1, 1]],
    [[1, 1, 1]], [[1], [1], [1]], [[1, 0], [1, 1]],
    [[0, 1], [1, 1]], [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]], [[1, 0], [1, 0], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
]

def clear(): os.system('clear')

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def gambar_papan(papan, kursor_r, kursor_c, bentuk, warna_blok, skor, antrean):
    clear()
    print(f"=== 🧱 BLOCK BLAST (MOUSE MODE) ===")
    print(f"Skor: {skor}")
    print("Gerakkan: W A S D | Taruh Blok: ENTER | Keluar: Q")
    print("=" * 25)
    
    tampilan = [row[:] for row in papan]
    
    for r in range(len(bentuk)):
        for c in range(len(bentuk[r])):
            if bentuk[r][c] == 1:
                rr, cc = kursor_r + r, kursor_c + c
                if 0 <= rr < BARIS and 0 <= cc < KOLOM:
                    if r == 0 and c == 0:
                        tampilan[rr][cc] = KURSOR_WARNA
                    else:
                        tampilan[rr][cc] = warna_blok

    for row in tampilan:
        print(" ".join(row))
    print("=" * 25)
    
    print("Antrean Blok Selanjutnya:")
    for i, (b, w) in enumerate(antrean):
        print(f"Blok {i+1}: ", end="")
        for baris in b:
            print("".join(w if x == 1 else "  " for x in baris), end="  ")
        print()

def cek_muat(papan, bentuk, r_pos, c_pos):
    for r in range(len(bentuk)):
        for c in range(len(bentuk[r])):
            if bentuk[r][c] == 1:
                if r_pos + r >= BARIS or c_pos + c < 0 or c_pos + c >= KOLOM: return False
                if papan[r_pos + r][c_pos + c] != KOSONG: return False
    return True

def cek_ledakan(papan):
    skor_tambah = 0
    baris_hapus = []
    kolom_hapus = []
    
    for r in range(BARIS):
        if all(cell != KOSONG for cell in papan[r]): baris_hapus.append(r)
    for c in range(KOLOM):
        if all(papan[r][c] != KOSONG for r in range(BARIS)): kolom_hapus.append(c)
            
    for r in baris_hapus:
        for c in range(KOLOM): papan[r][c] = KOSONG
        skor_tambah += 10
        
    for c in kolom_hapus:
        for r in range(BARIS): papan[r][c] = KOSONG
        skor_tambah += 10
        
    if len(baris_hapus) + len(kolom_hapus) > 1: skor_tambah += 50
    return skor_tambah

def main():
    clear()
    papan = [[KOSONG for _ in range(KOLOM)] for _ in range(BARIS)]
    skor = 0
    kursor_r = 0
    kursor_c = 0
    
    antrean = []
    for _ in range(3):
        antrean.append((random.choice(BENTUK), random.choice(WARNA)))
        
    while True:
        bentuk, warna = antrean[0]
        
        if kursor_r + len(bentuk) > BARIS: kursor_r = BARIS - len(bentuk)
        if kursor_c + len(bentuk[0]) > KOLOM: kursor_c = KOLOM - len(bentuk[0])
        if kursor_r < 0: kursor_r = 0
        if kursor_c < 0: kursor_c = 0
        
        gambar_papan(papan, kursor_r, kursor_c, bentuk, warna, skor, antrean)
        cmd = get_key()
        
        if cmd == 'q': break
        elif cmd in ['w', 'W']: kursor_r -= 1
        elif cmd in ['s', 'S']: kursor_r += 1
        elif cmd in ['a', 'A']: kursor_c -= 1
        elif cmd in ['d', 'D']: kursor_c += 1
        elif cmd in ['\r', '\n', ' ']: 
            if cek_muat(papan, bentuk, kursor_r, kursor_c):
                # Hitung jumlah kotak yang ditaruh buat nambah skor
                jumlah_kotak = sum(sum(baris) for baris in bentuk)
                
                for r in range(len(bentuk)):
                    for c in range(len(bentuk[r])):
                        if bentuk[r][c] == 1:
                            papan[kursor_r + r][kursor_c + c] = warna
                            
                # Tambah skor dari jumlah kotak
                skor += jumlah_kotak
                
                # Tambah skor dari ledakan
                skor += cek_ledakan(papan)
                
                antrean.pop(0)
                antrean.append((random.choice(BENTUK), random.choice(WARNA)))
                
                penuh = True
                for r in range(BARIS):
                    for c in range(KOLOM):
                        if papan[r][c] == KOSONG:
                            if cek_muat(papan, antrean[0][0], r, c):
                                penuh = False
                                break
                    if not penuh: break
                
                if penuh:
                    clear()
                    print("\n" * 5)
                    print("=" * 30)
                    print(f"   SKOR AKHIR LU: {skor}")
                    print("=" * 30)
                    print("\n   🗿  P A P A N   P E N U H  🗿\n")
                    break

if __name__ == "__main__":
    main()
