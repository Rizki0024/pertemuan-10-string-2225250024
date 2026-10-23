# LATIHAN 5: SPLIT DAN JOIN

print("=" * 40)
print("LATIHAN 5: SPLIT DAN JOIN".center(40))
print("=" * 40)

# LANGKAH 1: Menerima input kalimat
print("\n" + "-" * 40)
print("MASUKKAN KALIMAT".center(40))
print("-" * 40)

kalimat = input("Masukkan kalimat Anda: ")

# LANGKAH 2: Memecah kalimat menjadi kata
kata = kalimat.split()

# LANGKAH 3: Menggabungkan kata dengan tanda hubung
hasil_join = "-".join(kata)

# LANGKAH 4: Menampilkan hasil
print("\n" + "-" * 40)
print("HASIL SPLIT DAN JOIN".center(40))
print("-" * 40)
print("Kalimat asli       :", kalimat)
print("Daftar kata        :", kata)
print("Jumlah kata        :", len(kata))
print("Hasil dengan tanda hubung:", hasil_join)

print("=" * 40)
print("PROGRAM SELESAI".center(40))
print("=" * 40)