# visualisasi data dengan matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('penjualan_nusantaramart.csv')

# Histogram distribusi rating pelanggan
plt.figure(figsize=(7,5))
sns.histplot(data=data, x='rating_pelanggan', bins=5, color='seagreen')
plt.title('Distribusi Rating Pelanggan')
plt.xlabel('Rating')
plt.ylabel('Frekuensi')
plt.show()
# Boxplot jumlah pembelian per kategori (deteksi outlier)
plt.figure(figsize=(8,5))
sns.boxplot(data=data, x='kategori_produk', y='jumlah')
plt.title('Sebaran Jumlah Pembelian per Kategori Produk')
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()