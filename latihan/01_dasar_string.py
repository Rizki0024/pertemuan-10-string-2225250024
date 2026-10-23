# LATIHAN 1: DASAR STRING

print("=" * 40)
print("LATIHAN 1: DASAR STRING".center(40))
print("=" * 40)

# LANGKAH 1: Membuat teks
teks = "Algoritma"

print("\n" + "-" * 40)
print("DATA AWAL".center(40))
print("-" * 40)
print("Teks yang digunakan :", teks)

# LANGKAH 2: Mengolah string
panjang = len(teks)
huruf_besar = teks.upper()
huruf_kecil = teks.lower()

# LANGKAH 3: Menampilkan hasil
print("\n" + "-" * 40)
print("HASIL PENGOLAHAN STRING".center(40))
print("-" * 40)
print("Teks asli     :", teks)
print("Panjang teks  :", panjang)
print("Huruf besar   :", huruf_besar)
print("Huruf kecil   :", huruf_kecil)

print("=" * 40)
print("PROGRAM SELESAI".center(40))
print("=" * 40)