# visualisasi data dengan matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('penjualan_nusantaramart.csv')
total_kategori = data.groupby('kategori_produk')['total'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=total_kategori.index, y=total_kategori.values, palette='viridis')
plt.title('Total Penjualan per Kategori Produk')
plt.xlabel('Kategori Produk')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()