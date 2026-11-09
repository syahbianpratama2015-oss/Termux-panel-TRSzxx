n = input("Masukkan angka (pisah pakai koma): ").split(',')
angka = [float(x) for x in n]
print("Rata-rata:", sum(angka) / len(angka))
