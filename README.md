# Pertemuan 10 — String dan Pengolahan Teks dalam Python

## 1. Identitas

- **Nama:** Rizki Ramadan
- **NIM:** 2225250024
- **Kelas:** 3F
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Pertemuan:** 10

## 2. Tujuan

Tugas ini bertujuan untuk memahami dan menerapkan operasi string dalam Python, meliputi akses karakter, slicing, method string, pembersihan teks, normalisasi data, pemisahan dan penggabungan kata, serta pencarian kata.

Selain itu, tugas ini melatih penggunaan fungsi, pengujian program melalui VS Code, dokumentasi dengan README, dan pengumpulan kode menggunakan GitHub.

## 3. Struktur Folder

```text
pertemuan-10-string-2225250024/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_string.py
│   ├── 02_indeks_slicing.py
│   ├── 03_method_string.py
│   ├── 04_bersihkan_teks.py
│   ├── 05_split_join.py
│   └── 06_pencarian_kata.py
└── tugas/
    └── normalisasi_data_mahasiswa.py
```

## 4. Daftar Program

| No. | Nama File | Keterangan |
|---|---|---|
| 1 | `01_dasar_string.py` | Menampilkan string, panjang teks, dan perubahan huruf |
| 2 | `02_indeks_slicing.py` | Mengakses karakter dan mengambil sebagian string |
| 3 | `03_method_string.py` | Menggunakan `strip()`, `title()`, dan `upper()` |
| 4 | `04_bersihkan_teks.py` | Membersihkan spasi berlebih dan menormalkan teks |
| 5 | `05_split_join.py` | Memecah dan menggabungkan kata |
| 6 | `06_pencarian_kata.py` | Memeriksa, menghitung, dan mencari kata |
| 7 | `normalisasi_data_mahasiswa.py` | Menormalkan nama dan kode kelas, menghitung kata, serta membuat inisial |

## 5. Cara Menjalankan Program

1. Buka folder proyek melalui Visual Studio Code.
2. Pastikan Python 3 sudah terpasang.
3. Buka terminal VS Code.
4. Jalankan program menggunakan perintah berikut.

Contoh menjalankan latihan:

```powershell
python latihan/01_dasar_string.py
```

Menjalankan tugas utama:

```powershell
python tugas/normalisasi_data_mahasiswa.py
```

Masukkan nama mahasiswa dan kode kelas sesuai permintaan program.

## 6. Algoritma Tugas Utama

Program normalisasi data mahasiswa menggunakan langkah-langkah berikut:

1. Menerima input nama lengkap dan kode kelas.
2. Menghapus spasi di awal dan akhir nama.
3. Merapikan spasi berlebih di antara kata.
4. Mengubah nama menjadi format title case.
5. Memecah nama menjadi daftar kata menggunakan `split()`.
6. Menghitung jumlah kata pada nama.
7. Mengambil huruf pertama setiap kata untuk membentuk inisial.
8. Mengubah kode kelas menjadi huruf besar.
9. Menggabungkan bagian kode kelas menggunakan tanda hubung.
10. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

Program menggunakan tiga fungsi, yaitu `normalisasi_nama()`, `buat_inisial()`, dan `normalisasi_kode()`.

## 7. Hasil Pengujian

| No. | Input Nama | Input Kode | Hasil yang Diharapkan | Status |
|---|---|---|---|---|
| 1 | `aan hendrayana` | `pmat a 2026` | `Aan Hendrayana`, `PMAT-A-2026`, `2`, `AH` | [Isi setelah diuji] |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | `Fathiyyah Muthmainnah`, `KELAS-B`, `2`, `FM` | [Isi setelah diuji] |
| 3 | `BUDI` | `pmtk 01` | `Budi`, `PMTK-01`, `1`, `B` | [Isi setelah diuji] |
| 4 | `siti nur aisyah` | `kelas c` | `Siti Nur Aisyah`, `KELAS-C`, `3`, `SNA` | [Isi setelah diuji] |

Catatan: status pengujian harus diisi berdasarkan hasil eksekusi program yang sebenarnya. Tandai **Lulus** apabila seluruh hasil aktual sesuai dengan hasil yang diharapkan.

## 8. Refleksi

Melalui tugas ini, saya mempelajari bahwa string dapat digunakan untuk mengolah dan menormalkan data teks yang formatnya tidak konsisten. Method seperti `strip()`, `title()`, dan `upper()` membantu menyeragamkan data, sedangkan `split()` dan `join()` membantu memisahkan serta menggabungkan kata.

Saya juga memahami bahwa string bersifat immutable, sehingga proses pengolahan menghasilkan string baru. Penggunaan fungsi membuat kode lebih terstruktur dan dapat digunakan kembali.

Salah satu hal yang perlu diperhatikan adalah spasi berlebih pada nama dan kode kelas. Hal tersebut dapat ditangani dengan membersihkan input sebelum melakukan proses berikutnya.

## 9. Kesimpulan

Operasi string Python dapat digunakan untuk membersihkan, menormalkan, mencari, dan mengolah teks. Melalui enam latihan dan tugas normalisasi data mahasiswa, saya menerapkan method string, slicing, `split()`, `join()`, serta fungsi untuk menghasilkan data yang lebih konsisten.

Pengujian dan dokumentasi membantu memastikan program berjalan sesuai spesifikasi. Git dan GitHub digunakan untuk mencatat perkembangan pekerjaan dan mengumpulkan hasil tugas.

## 10. Sumber Referensi

1. Bahan Ajar Algoritma dan Pemrograman, Pertemuan 10: String dan Pengolahan Teks dalam Python, Tahun Ajaran 2026/2027 Ganjil.
2. OpenAI. (2026). ChatGPT [Alat bantu kecerdasan buatan]. https://chatgpt.com/.

Bantuan AI digunakan untuk membantu memahami materi dan menyusun contoh solusi. Kode, pengujian, dan penjelasan akhir akan diperiksa kembali agar dapat dipahami dan dipertanggungjawabkan.
