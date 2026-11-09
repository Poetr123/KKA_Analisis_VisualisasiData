# Jawaban Tugas Analisis Bagian C
## Modul Ajar KKA 3 — Analisis dan Visualisasi Data (AVD)

**Dataset:** `penjualan_nusantaramart.csv`  
**Sumber kode praktikum:** `praktikum1.py` sampai `praktikum6.py`

---

## Ringkasan Data

Berdasarkan dataset yang digunakan oleh keenam praktikum:

- Jumlah data: **220 transaksi** dengan **10 kolom**.
- Periode transaksi: **Januari–Juni 2026**.
- Tidak ditemukan missing value pada seluruh kolom.
- Total penjualan seluruh transaksi: **Rp52.467.000**.
- Rata-rata nilai transaksi: **Rp238.486,36**.
- Median nilai transaksi: **Rp125.000**.

### Ringkasan berdasarkan kategori produk

| Kategori Produk | Jumlah Transaksi | Rata-rata Total per Transaksi | Total Penjualan |
|---|---:|---:|---:|
| Elektronik | 48 | Rp363.541,67 | Rp17.450.000 |
| Fashion | 50 | Rp353.900,00 | Rp17.695.000 |
| Olahraga | 42 | Rp209.071,43 | Rp8.781.000 |
| Kesehatan | 37 | Rp148.972,97 | Rp5.512.000 |
| Makanan & Minuman | 43 | Rp70.441,86 | Rp3.029.000 |

---

## Latihan 1 — Eksplorasi Data & Statistika Deskriptif dengan Pandas

### Tugas Analisis 1

**1. Kategori produk apa yang memiliki rata-rata nilai transaksi (`total`) tertinggi?**

Kategori **Elektronik** memiliki rata-rata nilai transaksi tertinggi, yaitu sekitar **Rp363.541,67 per transaksi**. Posisi kedua adalah Fashion dengan rata-rata Rp353.900,00 per transaksi. Artinya, secara rata-rata, satu transaksi pada kategori Elektronik memiliki nilai pembelian paling besar dibandingkan kategori lainnya.

**2. Apakah ada kolom yang memiliki data kosong (missing value)? Bagaimana cara mengeceknya dari output `df.info()`?**

Tidak ada kolom yang memiliki missing value. Hal ini dapat diketahui dari output `df.info()` karena seluruh 10 kolom menunjukkan jumlah nilai *non-null* sebanyak **220**, sama dengan jumlah baris dataset. Jika terdapat missing value, jumlah *non-null* pada kolom tersebut akan lebih kecil dari 220. Pemeriksaan tambahan juga dapat dilakukan menggunakan `df.isnull().sum()`.

**3. Bandingkan nilai mean dan median kolom `total` secara keseluruhan. Apa yang bisa kamu simpulkan tentang sebaran datanya?**

Mean kolom `total` adalah **Rp238.486,36**, sedangkan mediannya **Rp125.000**. Mean jauh lebih besar daripada median. Hal ini menunjukkan bahwa distribusi nilai transaksi cenderung **miring ke kanan (right-skewed)**. Beberapa transaksi dengan nilai sangat besar menaikkan rata-rata, sehingga mean menjadi lebih tinggi daripada nilai tengah. Untuk menggambarkan nilai transaksi yang umum, median dapat menjadi ukuran yang lebih mewakili karena tidak terlalu terpengaruh oleh transaksi ekstrem.

---

## Latihan 2 — Visualisasi Perbandingan dengan Bar Chart

### Tugas Analisis 2

**1. Kategori apa yang menyumbang penjualan tertinggi dan terendah?**

Berdasarkan total penjualan setiap kategori:

- **Tertinggi:** Fashion, dengan total penjualan **Rp17.695.000**.
- **Terendah:** Makanan & Minuman, dengan total penjualan **Rp3.029.000**.

Elektronik berada sangat dekat dengan Fashion, dengan total penjualan Rp17.450.000. Jadi, Fashion merupakan penyumbang total penjualan terbesar, sedangkan Makanan & Minuman merupakan penyumbang terkecil.

**2. Menurutmu, apa rekomendasi bisnis yang bisa diberikan kepada manajer Nusantara Mart berdasarkan grafik ini?**

Manajer dapat memprioritaskan ketersediaan stok dan promosi pada kategori **Fashion** karena menghasilkan total penjualan tertinggi. Kategori Elektronik juga perlu diperhatikan karena total penjualannya hampir sama dengan Fashion dan rata-rata nilai transaksinya justru paling tinggi. Sementara itu, kategori Makanan & Minuman dapat dievaluasi melalui promosi bundling, penempatan produk, atau penawaran tambahan saat pelanggan membeli produk kategori lain. Evaluasi lebih lanjut tetap diperlukan sebelum mengurangi stok atau menghentikan produk, karena total penjualan saja belum menunjukkan keuntungan bersih.

---

## Latihan 3 — Visualisasi Tren dengan Line Chart

### Tugas Analisis 3

**1. Bulan apa yang memiliki penjualan tertinggi? Menurutmu, apa kemungkinan penyebabnya?**

Bulan dengan total penjualan tertinggi adalah **Mei 2026**, yaitu **Rp13.585.000**. Pada bulan tersebut terdapat 37 transaksi dengan rata-rata nilai transaksi sekitar Rp367.162,16. Jumlah transaksi Mei bukan yang terbanyak, tetapi nilai rata-rata transaksinya paling tinggi. Salah satu kemungkinan penyebabnya adalah adanya beberapa pembelian dengan kuantitas atau nilai transaksi besar. Contohnya, terdapat transaksi 40 unit pada kategori Olahraga dan transaksi 25 unit pada kategori Elektronik di bulan Mei. Dataset tidak memuat informasi promosi atau kegiatan pemasaran, sehingga penyebab pastinya tidak dapat dipastikan hanya dari data ini.

**2. Apakah tren penjualan cenderung naik, turun, atau fluktuatif? Jelaskan.**

Tren penjualan **fluktuatif**. Total penjualan meningkat secara bertahap dari Januari sampai Mei, kemudian turun cukup tajam pada Juni.

| Bulan 2026 | Total Penjualan |
|---|---:|
| Januari | Rp6.147.000 |
| Februari | Rp7.314.000 |
| Maret | Rp8.592.000 |
| April | Rp9.837.000 |
| Mei | Rp13.585.000 |
| Juni | Rp6.992.000 |

Penjualan tertinggi terjadi pada Mei, lalu turun sekitar 48,5% pada Juni. Jumlah transaksi Juni sebanyak 39, bahkan sedikit lebih banyak daripada Mei yang berjumlah 37 transaksi. Dengan demikian, penurunan Juni lebih berkaitan dengan nilai rata-rata pembelian per transaksi yang lebih rendah, bukan semata-mata karena jumlah transaksinya berkurang.

---

## Latihan 4 — Visualisasi Hubungan dengan Scatter Plot

### Tugas Analisis 4

**1. Apakah terlihat pola hubungan antara jumlah barang dan total nilai transaksi? Jelaskan hubungan tersebut (positif/negatif/tidak berhubungan).**

Terlihat hubungan **positif** antara jumlah barang yang dibeli dan total nilai transaksi. Secara umum, semakin banyak barang yang dibeli, semakin besar total nilai transaksinya. Pola ini masuk akal karena nilai `total` dihitung dari jumlah barang dikalikan harga satuan. Dari perhitungan korelasi Pearson pada dataset, hubungan keduanya sekitar **0,854**, yang menunjukkan hubungan positif yang kuat. Meskipun demikian, besar total juga dipengaruhi oleh harga satuan setiap produk, sehingga transaksi dengan jumlah barang sama belum tentu memiliki total yang sama.

**2. Apakah ada titik data yang terlihat jauh dari pola umum (kemungkinan outlier)? Sebutkan kategorinya jika terlihat dari warna.**

Ada beberapa titik dengan jumlah pembelian dan nilai transaksi yang jauh lebih tinggi daripada sebagian besar data. Titik yang paling menonjol terdapat pada kategori berikut:

- **Elektronik:** 40 unit dengan total Rp3.400.000; serta transaksi 25 unit dengan total Rp2.375.000 dan Rp2.125.000.
- **Olahraga:** 40 unit dengan total Rp1.600.000 dan 25 unit dengan total Rp800.000.
- **Kesehatan:** 25 unit dengan total Rp1.500.000.

Titik-titik tersebut berpotensi menjadi outlier karena kuantitas dan nilai transaksinya jauh lebih besar daripada pola mayoritas transaksi. Kemungkinan penyebabnya antara lain pembelian dalam jumlah besar, pembelian untuk dijual kembali, pesanan kelompok, atau kesalahan pencatatan. Data yang tersedia belum cukup untuk memastikan penyebab sebenarnya.

---

## Latihan 5 — Visualisasi Distribusi & Deteksi Outlier (Histogram & Boxplot)

### Tugas Analisis 5

**1. Bagaimana bentuk distribusi rating pelanggan? Apakah cenderung tinggi, rendah, atau merata?**

Distribusi rating pelanggan cenderung **tinggi**, karena sebagian besar pelanggan memberikan rating 4 atau 5.

| Rating | Frekuensi |
|---:|---:|
| 2 | 4 |
| 3 | 41 |
| 4 | 92 |
| 5 | 83 |

Sebanyak **175 dari 220 transaksi (79,5%)** memiliki rating 4 atau 5. Rating yang paling sering muncul adalah 4, yaitu 92 kali. Rating 2 hanya muncul 4 kali dan tidak terdapat rating 1. Hal ini menunjukkan bahwa penilaian pelanggan secara umum cukup baik, meskipun masih ada sebagian kecil pelanggan yang memberikan penilaian lebih rendah.

**2. Kategori produk mana yang memiliki titik-titik di luar kotak boxplot (outlier)? Apa kemungkinan penyebabnya (misalnya pembelian oleh reseller)?**

Berdasarkan boxplot jumlah pembelian per kategori dan aturan batas 1,5 × IQR, titik di luar whisker ditemukan pada:

| Kategori | Jumlah Pembelian yang Menjadi Outlier |
|---|---|
| Elektronik | 40, 25, dan 25 unit |
| Fashion | 8 unit |
| Kesehatan | 25 unit |
| Olahraga | 40, 25, dan 8 unit |
| Makanan & Minuman | Tidak ditemukan |

Kategori Elektronik dan Olahraga memiliki beberapa titik dengan jumlah pembelian yang sangat tinggi. Kategori Fashion dan Kesehatan juga memiliki masing-masing satu titik di luar whisker. Sementara itu, Makanan & Minuman tidak menunjukkan outlier berdasarkan aturan tersebut.

Kemungkinan penyebabnya adalah pembelian oleh reseller, pembelian grosir, pesanan untuk kelompok atau organisasi, maupun kesalahan input jumlah barang. Untuk memastikan penyebabnya, pihak toko perlu memeriksa detail transaksi yang bersangkutan. Outlier tidak boleh langsung dihapus karena bisa saja merupakan transaksi besar yang benar-benar terjadi.

---

## Latihan 6 — Menggabungkan Grafik dalam Dashboard Sederhana

### Tugas Analisis 6

**1. Menurutmu, apa keuntungan menyajikan beberapa grafik dalam satu dashboard dibandingkan grafik terpisah-pisah?**

Dashboard membuat beberapa informasi penting dapat dilihat dalam satu tampilan, sehingga analisis menjadi lebih praktis dan mudah dibandingkan membuka grafik satu per satu. Manajer dapat membandingkan total penjualan setiap kategori melalui bar chart, melihat perubahan penjualan bulanan melalui line chart, memahami sebaran rating pelanggan melalui histogram, serta menemukan variasi dan outlier jumlah pembelian melalui boxplot. Hubungan antarinformasi juga lebih mudah terlihat karena semua grafik disajikan secara bersamaan. Dengan demikian, dashboard membantu pembaca memperoleh gambaran umum kondisi penjualan secara lebih cepat.

**2. Jika kamu adalah manajer Nusantara Mart, keputusan bisnis apa yang akan kamu ambil setelah melihat dashboard ini?**

Sebagai manajer, saya akan memprioritaskan pengelolaan stok dan promosi pada kategori Fashion dan Elektronik karena keduanya menghasilkan total penjualan terbesar. Elektronik juga memiliki rata-rata nilai transaksi tertinggi, sehingga stok produk kategori ini perlu dipantau dengan baik. Saya akan mengevaluasi penurunan penjualan pada Juni dengan memeriksa faktor seperti perubahan permintaan, produk yang tersedia, dan kegiatan promosi. Selain itu, transaksi dengan jumlah pembelian yang menjadi outlier akan diperiksa untuk mengetahui apakah berasal dari pembelian grosir, reseller, atau kesalahan pencatatan. Karena 79,5% rating berada pada angka 4 atau 5, kualitas layanan perlu dipertahankan, sementara masukan dari pelanggan yang memberikan rating 2 atau 3 perlu ditinjau. Untuk kategori Makanan & Minuman yang total penjualannya paling rendah, saya akan mencoba promosi bundling atau penawaran tambahan dan mengevaluasi hasilnya sebelum mengambil keputusan stok lebih lanjut.

---

## Catatan Interpretasi

1. **Rata-rata transaksi tertinggi tidak sama dengan total penjualan tertinggi.** Elektronik memiliki rata-rata transaksi tertinggi, sedangkan Fashion menghasilkan total penjualan terbesar.
2. **Outlier bukan otomatis kesalahan data.** Transaksi dalam jumlah besar perlu diperiksa terlebih dahulu sebelum diputuskan untuk dipertahankan, dikoreksi, atau dikeluarkan dari analisis.
3. **Kemungkinan penyebab bukan fakta yang sudah terbukti.** Dataset tidak menyediakan informasi mengenai kampanye promosi, identitas reseller, atau alasan pembelian. Oleh karena itu, penyebab kenaikan atau penurunan penjualan hanya dapat disampaikan sebagai dugaan yang perlu diverifikasi.

**Kesimpulan:** Berdasarkan keenam latihan, performa penjualan Nusantara Mart paling kuat pada kategori Fashion dan Elektronik. Penjualan bulanan mencapai puncak pada Mei 2026, hubungan jumlah barang dengan nilai transaksi bersifat positif, dan mayoritas rating pelanggan berada pada kategori tinggi. Informasi tersebut dapat digunakan sebagai dasar awal untuk pengelolaan stok, promosi, pemeriksaan transaksi besar, dan peningkatan layanan pelanggan.
