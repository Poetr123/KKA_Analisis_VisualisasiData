# Eksplorasi Data & Statistika Deskriptif dengan Pandas
import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv('penjualan_nusantaramart.csv')

# Menampilkan 5 baris pertama dari dataset
print(data.head())

# Menampilkan statistik deskriptif dari dataset
print(data.describe())

# Menampilkan informasi tentang dataset, termasuk tipe data
# dan jumlah nilai yang tidak kosong
print(data.info())

# Rata-rata total pembelian per kategori
rata_kategori = data.groupby('kategori_produk')['total'].mean()

# Menampilkan rata-rata total pembelian per kategori,
# diurutkan dari yang tertinggi
print(rata_kategori.sort_values(ascending=False))