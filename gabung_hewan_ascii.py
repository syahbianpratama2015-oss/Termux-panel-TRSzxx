import random

print("=== 🐾 GABUNGKAN HEWAN LUCU ===")
h1 = input("Hewan pertama: ").lower()
h2 = input("Hewan kedua: ").lower()

# Logika motong nama (Ambil 3-4 huruf depan, sisanya belakang)
depan = h1[:3] if len(h1) > 3 else h1
belakang = h2[-3:] if len(h2) > 3 else h2
nama_baru = (depan + belakang).capitalize()

# Kumpulan gambar ASCII lucu
gambar = [
    r"""
       (\_/)
       (o.o)  <- {nama} lagi bingung
       (> <)
    """,
    r"""
        /\_/\
       ( o.o )
        > ^ <  <- {nama} ngambek
    """,
    r"""
       ___
      /   \  <- {nama} siap beraksi
     | o o |
      \___/
    """
]

pilihan_gambar = random.choice(gambar).format(nama=nama_baru)

print(f"\n✨ Hasil gabungan: {nama_baru} ✨")
print(pilihan_gambar)
