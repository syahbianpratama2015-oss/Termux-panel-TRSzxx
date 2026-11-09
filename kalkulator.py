def kalkulator():
    print("=== KALKULATOR SAKTI ===")
    print("Ketik 'keluar' untuk berhenti.\n")
    
    while True:
        try:
            # Minta input dari user
            angka1 = input("Masukkan angka pertama (atau 'keluar'): ")
            if angka1.lower() == 'keluar':
                print("Dadah! Program berhenti.")
                break
                
            operator = input("Pilih operator (+, -, *, /): ")
            angka2 = input("Masukkan angka kedua: ")
            
            # Ubah teks input jadi angka desimal (float)
            num1 = float(angka1)
            num2 = float(angka2)
            
            # Logika perhitungan
            if operator == '+':
                hasil = num1 + num2
            elif operator == '-':
                hasil = num1 - num2
            elif operator == '*':
                hasil = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("❌ Error: Gak bisa dibagi nol bang!\n")
                    continue # Balik ke awal loop
                hasil = num1 / num2
            else:
                print("❌ Operator gak dikenal!\n")
                continue
                
            print(f"✅ Hasil: {num1} {operator} {num2} = {hasil}\n")
            print("-" * 25)
            
        except ValueError:
            # Ini pengaman kalau user ngetik huruf, bukan angka
            print("❌ Error: Masukkan angka yang bener dong, bukan huruf!\n")

# Jalankan programnya
kalkulator()
