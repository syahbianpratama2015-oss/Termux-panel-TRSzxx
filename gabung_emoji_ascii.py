import random

print("=== 🎭 GABUNGKAN EMOJI ===")
e1 = input("Emoji pertama (contoh: 🐱): ")
e2 = input("Emoji kedua (contoh: 🐶): ")

nama_baru = "Simbah_" + str(random.randint(10, 99))

gambar = [
    r"""
       [ {e1} ]
         |
       \ | /
      -- {e2} --
         |
       / | \
    """,
    r"""
       ({e1})
        \ /
         X
        / \
       ({e2})
    """
]

print(f"\n✨ Hasil gabungan: {nama_baru} ✨")
print(random.choice(gambar).format(e1=e1, e2=e2))
