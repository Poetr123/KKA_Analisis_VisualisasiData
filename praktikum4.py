# visualisasi data dengan matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('penjualan_nusantaramart.csv')

plt.figure(figsize=(7,5))
sns.scatterplot(data=data, x='jumlah', y='total', hue='kategori_produk')
plt.title('Hubungan Jumlah Pembelian dengan Total Nilai Transaksi')
plt.xlabel('Jumlah Barang')
plt.ylabel('Total (Rp)')
plt.tight_layout()
plt.show()