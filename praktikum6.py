
# Visualisasi data dengan Matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Membaca data CSV
data = pd.read_csv('penjualan_nusantaramart.csv')

# Menghitung total penjualan per kategori
total_kategori = data.groupby('kategori_produk')['total'].sum()

# Menghitung tren penjualan bulanan
data['tanggal'] = pd.to_datetime(data['tanggal'])
data['bulan'] = data['tanggal'].dt.to_period('M')

tren_bulanan = data.groupby('bulan')['total'].sum()

# Membuat area grafik 2x2
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# Grafik 1: Total Penjualan per Kategori
sns.barplot(
    x=total_kategori.values,
    y=total_kategori.index,
    ax=axes[0, 0]
)
axes[0, 0].set_title('Total Penjualan per Kategori')
axes[0, 0].set_xlabel('Total Penjualan')
axes[0, 0].set_ylabel('Kategori Produk')

# Grafik 2: Tren Penjualan Bulanan
axes[0, 1].plot(
    tren_bulanan.index.astype(str),
    tren_bulanan.values,
    marker='o'
)
axes[0, 1].set_title('Tren Penjualan Bulanan')
axes[0, 1].set_xlabel('Bulan')
axes[0, 1].set_ylabel('Total Penjualan')
axes[0, 1].tick_params(axis='x', rotation=45)

# Grafik 3: Distribusi Rating Pelanggan
sns.histplot(
    data=data,
    x='rating_pelanggan',
    bins=5,
    ax=axes[1, 0]
)
axes[1, 0].set_title('Distribusi Rating Pelanggan')
axes[1, 0].set_xlabel('Rating Pelanggan')
axes[1, 0].set_ylabel('Frekuensi')

# Grafik 4: Sebaran Jumlah per Kategori
sns.boxplot(
    data=data,
    x='kategori_produk',
    y='jumlah',
    ax=axes[1, 1]
)
axes[1, 1].set_title('Sebaran Jumlah per Kategori')
axes[1, 1].set_xlabel('Kategori Produk')
axes[1, 1].set_ylabel('Jumlah Terjual')
axes[1, 1].tick_params(axis='x', rotation=45)

# Merapikan dan menampilkan grafik
plt.tight_layout()
plt.show()
