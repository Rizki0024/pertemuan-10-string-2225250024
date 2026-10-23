# LATIHAN 3: METHOD STRING

print("=" * 40)
print("LATIHAN 3: METHOD STRING".center(40))
print("=" * 40)

# LANGKAH 1: Menerima input nama
print("\n" + "-" * 40)
print("MASUKKAN DATA".center(40))
print("-" * 40)

nama = input("Masukkan nama Anda: ")

# LANGKAH 2: Mengolah nama
nama_bersih = nama.strip()
nama_title = nama_bersih.title()
nama_besar = nama_bersih.upper()
nama_kecil = nama_bersih.lower()

# LANGKAH 3: Menampilkan hasil
print("\n" + "-" * 40)
print("HASIL PENGOLAHAN NAMA".center(40))
print("-" * 40)
print("Nama asli       :", repr(nama))
print("Nama tanpa spasi:", nama_bersih)
print("Format title    :", nama_title)
print("Huruf besar     :", nama_besar)
print("Huruf kecil     :", nama_kecil)

print("=" * 40)
print("PROGRAM SELESAI".center(40))
print("=" * 40)