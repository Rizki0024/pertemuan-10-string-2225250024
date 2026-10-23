
# TUGAS 4: NORMALISASI DATA MAHASISWA
# Pertemuan 10 - String dan Pengolahan Teks dalam Python

print("=" * 45)
print("NORMALISASI DATA MAHASISWA".center(45))
print("=" * 45)


# LANGKAH 1: Fungsi untuk menormalkan nama
def normalisasi_nama(nama):
    nama = " ".join(nama.strip().split())
    return nama.title()


# LANGKAH 2: Fungsi untuk membuat inisial
def buat_inisial(nama):
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    inisial = "".join(item[0] for item in kata)
    return inisial


# LANGKAH 3: Fungsi untuk menormalkan kode kelas
def normalisasi_kode(kode):
    bagian_kode = kode.strip().upper().split()
    return "-".join(bagian_kode)


# LANGKAH 4: Meminta input pengguna
print("\n" + "-" * 45)
print("MASUKKAN DATA MAHASISWA".center(45))
print("-" * 45)

nama = input("Masukkan nama Anda  : ")
kode = input("Masukkan kode kelas : ")


# LANGKAH 5: Memproses input
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama)


# LANGKAH 6: Menampilkan hasil
print("\n" + "=" * 45)
print("HASIL NORMALISASI DATA".center(45))
print("=" * 45)

print("Nama bersih  :", nama_bersih)
print("Kode kelas   :", kode_bersih)
print("Jumlah kata  :", jumlah_kata)
print("Inisial      :", inisial)

print("=" * 45)
print("PROGRAM SELESAI".center(45))
print("=" * 45)
