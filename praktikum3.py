# visualisasi data dengan matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('penjualan_nusantaramart.csv')

data['tanggal'] = pd.to_datetime(data['tanggal'])
data['bulan'] = data['tanggal'].dt.to_period('M')
tren_bulanan = data.groupby('bulan')['total'].sum()
plt.figure(figsize=(8,5))
plt.plot(tren_bulanan.index.astype(str), tren_bulanan.values, marker='o', color='crimson')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan (Rp)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()