# LATIHAN 6: PENCARIAN KATA

print("=" * 40)
print("LATIHAN 6: PENCARIAN KATA".center(40))
print("=" * 40)

# LANGKAH 1: Menerima input teks dan kata pencarian
print("\n" + "-" * 40)
print("MASUKKAN DATA".center(40))
print("-" * 40)

teks = input("Masukkan teks Anda: ")
kata = input("Masukkan kata yang dicari: ")

# LANGKAH 2: Menyamakan huruf menjadi kecil
teks_bersih = teks.lower()
kata_bersih = kata.lower()

# LANGKAH 3: Melakukan pencarian
ditemukan = kata_bersih in teks_bersih
jumlah = teks_bersih.count(kata_bersih)
posisi = teks_bersih.find(kata_bersih)

# LANGKAH 4: Menampilkan hasil
print("\n" + "-" * 40)
print("HASIL PENCARIAN KATA".center(40))
print("-" * 40)
print("Teks yang dicari :", teks)
print("Kata pencarian   :", kata)
print("Kata ditemukan  :", ditemukan)
print("Jumlah kemunculan:", jumlah)
print("Posisi pertama   :", posisi)

print("=" * 40)
print("PROGRAM SELESAI".center(40))
print("=" * 40)