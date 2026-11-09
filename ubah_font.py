import os

# Kumpulan gaya font (Unicode)
def font_minecraft(teks):
    # Gaya kotak-kotak ala Minecraft
    return f"【 {teks.upper()} 】"

def font_gothic(teks):
    # Gaya huruf Gothic
    gothic = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅"
    abjad = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasil = ""
    for h in teks.upper():
        if h in abjad:
            hasil += gothic[abjad.index(h)]
        else:
            hasil += h
    return hasil

def font_bubble(teks):
    # Gaya huruf gelembung
    bubble = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"
    abjad = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    for h in teks.lower():
        if h in abjad:
            hasil += bubble[abjad.index(h)]
        else:
            hasil += h
    return hasil

def main():
    os.system("clear")
    print("=== 🔠 UBAH FONT TERMUX ===")
    print("1. Gaya Minecraft (Kotak)")
    print("2. Gaya Gothic (Keren)")
    print("3. Gaya Bubble (Lucu)")
    print("0. Kembali")
    
    pilih = input("\nPilih gaya [0-3]: ")
    if pilih == '0': return
    
    teks = input("Masukkan teks yang mau diubah: ")
    
    print("\n✨ HASILNYA:")
    if pilih == '1':
        print(font_minecraft(teks))
    elif pilih == '2':
        print(font_gothic(teks))
    elif pilih == '3':
        print(font_bubble(teks))
    else:
        print("❌ Pilihan salah!")
        
    print("\n💡 (Tekan lama buat nge-copy teks di atas)")

if __name__ == "__main__":
    main()
