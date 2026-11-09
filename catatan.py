import os

FILE = os.path.expanduser("~/catatan.txt")

def lihat():
    if not os.path.exists(FILE):
        print("\n📭 Belum ada catatan.")
        return
    print("\n=== 📝 DAFTAR CATATAN ===")
    with open(FILE, "r") as f:
        for i, line in enumerate(f, 1):
            print(f"{i}. {line.strip()}")
    print("========================\n")

def tambah():
    isi = input("Tulis catatan baru: ")
    with open(FILE, "a") as f:
        f.write(isi + "\n")
    print("✅ Catatan berhasil disimpan!")

def hapus():
    lihat()
    if not os.path.exists(FILE): return
    try:
        nomor = int(input("Masukkan nomor catatan yang mau dihapus: "))
        with open(FILE, "r") as f:
            lines = f.readlines()
        if 1 <= nomor <= len(lines):
            del lines[nomor - 1]
            with open(FILE, "w") as f:
                f.writelines(lines)
            print("🗑️ Catatan berhasil dihapus!")
        else:
            print("❌ Nomor tidak valid.")
    except ValueError:
        print("❌ Masukkan angka!")

def main():
    while True:
        print("=== 📒 MENU CATATAN ===")
        print("1. Lihat Catatan")
        print("2. Tambah Catatan")
        print("3. Hapus Catatan")
        print("0. Kembali")
        pilih = input("Pilih [0-3]: ")
        
        if pilih == '1': lihat()
        elif pilih == '2': tambah()
        elif pilih == '3': hapus()
        elif pilih == '0': break
        else: print("❌ Pilihan salah.")

if __name__ == "__main__":
    main()
