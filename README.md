# Website Katalog Sederhana dengan Django

## Identitas
- **Nama**: Naufal Aqil
- **NIM**: [Isi NIM Kamu di sini]

## Penjelasan Singkat Program
Proyek ini adalah sebuah website katalog produk sederhana yang dibangun menggunakan framework Django. Website ini bertujuan untuk menampilkan daftar produk beserta detailnya. Data produk yang ditampilkan menggunakan data _hardcoded_ (tidak menggunakan database).

Website ini memiliki empat halaman utama:
1. **Homepage** (`/`): Menampilkan ucapan selamat datang.
2. **Daftar Produk** (`/produk/`): Menampilkan daftar 3 produk (Laptop Gaming, Mouse Wireless, Keyboard Mekanik).
3. **Detail Produk** (`/produk/<id>/`): Menampilkan detail produk yang dipilih berdasarkan ID-nya.
4. **Kontak** (`/kontak/`): Menampilkan informasi kontak sederhana.

## Cara Menjalankan
1. Pastikan Anda telah menginstal Python dan Django.
2. Jalankan server lokal dengan perintah:
   ```bash
   python manage.py runserver
   ```
3. Buka browser dan akses `http://127.0.0.1:8000`.
