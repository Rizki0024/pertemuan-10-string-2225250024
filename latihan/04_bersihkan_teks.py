# LATIHAN 4: MEMBERSIHKAN TEKS

print("=" * 40)
print("LATIHAN 4: MEMBERSIHKAN TEKS".center(40))
print("=" * 40)

# LANGKAH 1: Menerima input teks
print("\n" + "-" * 40)
print("MASUKKAN TEKS".center(40))
print("-" * 40)

teks = input("Masukkan teks Anda: ")

# LANGKAH 2: Menghapus spasi di awal dan akhir
teks = teks.strip()

# LANGKAH 3: Memadatkan spasi berulang
while "  " in teks:
    teks = teks.replace("  ", " ")

# LANGKAH 4: Mengubah huruf awal menjadi kapital
hasil = teks.capitalize()

# LANGKAH 5: Menampilkan hasil
print("\n" + "-" * 40)
print("HASIL PEMBERSIHAN TEKS".center(40))
print("-" * 40)
print("Teks setelah dibersihkan:", hasil)
print("Panjang teks             :", len(hasil))

print("=" * 40)
print("PROGRAM SELESAI".center(40))
print("=" * 40)