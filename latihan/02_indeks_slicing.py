# LATIHAN 2: INDEKS DAN SLICING

print("=" * 40)
print("LATIHAN 2: INDEKS DAN SLICING".center(40))
print("=" * 40)

# LANGKAH 1: Menentukan teks
teks = "Pemrograman"

print("\n" + "-" * 40)
print("DATA AWAL".center(40))
print("-" * 40)
print("Teks yang digunakan :", teks)

# LANGKAH 2: Mengakses karakter
karakter_awal = teks[0]
karakter_akhir = teks[-1]

# LANGKAH 3: Mengambil bagian string
empat_karakter = teks[:4]
sisa_teks = teks[4:]
teks_terbalik = teks[::-1]

# LANGKAH 4: Menampilkan hasil
print("\n" + "-" * 40)
print("HASIL INDEKS DAN SLICING".center(40))
print("-" * 40)
print("Karakter pertama       :", karakter_awal)
print("Karakter terakhir      :", karakter_akhir)
print("Empat karakter pertama :", empat_karakter)
print("Karakter setelah indeks 3:", sisa_teks)
print("Teks terbalik          :", teks_terbalik)

print("=" * 40)
print("PROGRAM SELESAI".center(40))
print("=" * 40)