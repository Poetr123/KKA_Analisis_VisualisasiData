from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "viral_songs.csv"
CHART_DIR = BASE_DIR / "grafik"
CHART_DIR.mkdir(exist_ok=True)

REQUIRED_COLUMNS = {
    "track_id", "track_name", "artist", "genre", "release_year",
    "duration_sec", "danceability", "energy", "valence", "tempo_bpm",
    "acousticness", "instrumentalness", "speechiness", "liveness",
    "loudness_db", "streams", "viral"
}

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset tidak ditemukan: {DATA_FILE}. "
            "Pastikan viral_songs.csv berada satu folder dengan script."
        )

    df = pd.read_csv(DATA_FILE)
    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Kolom wajib tidak ditemukan: {sorted(missing_columns)}")

    # 1. Data loading dan pemeriksaan kualitas
    print("\\n=== DATA LOADING & INSPECTION ===")
    print("Shape:", df.shape)
    print("\\n5 baris pertama:\\n", df.head())
    print("\\nInformasi kolom:")
    df.info()
    print("\\nMissing value:\\n", df.isna().sum())
    print("\\nDuplikat identik:", df.duplicated().sum())
    print("track_id duplikat:", df["track_id"].duplicated().sum())
    print("\\nStatistik numerik:\\n", df.describe())

    # Data sudah lengkap menurut hasil pemeriksaan: tidak dilakukan drop/imputasi.
    if df.isna().any().any():
        print("\\nPERINGATAN: ditemukan missing value. Tinjau sebelum melanjutkan.")
    if df["track_id"].duplicated().any():
        print("\\nPERINGATAN: ditemukan track_id ganda. Tinjau sebelum melanjutkan.")

    # 2. Ringkasan statistik
    genre_summary = df.groupby("genre").agg(
        jumlah_lagu=("track_id", "count"),
        total_streams=("streams", "sum"),
        rata_rata_streams=("streams", "mean"),
        median_streams=("streams", "median"),
        lagu_viral=("viral", "sum"),
        tingkat_viral=("viral", "mean"),
    ).sort_values("tingkat_viral", ascending=False)

    year_summary = df.groupby("release_year").agg(
        jumlah_lagu=("track_id", "count"),
        rata_rata_streams=("streams", "mean"),
        total_streams=("streams", "sum"),
        tingkat_viral=("viral", "mean"),
    )

    print("\\n=== RINGKASAN GENRE ===\\n", genre_summary)
    print("\\n=== RINGKASAN TAHUN RILIS ===\\n", year_summary)
    print("\\nTotal streams:", int(df["streams"].sum()))
    print("Mean streams:", df["streams"].mean())
    print("Median streams:", df["streams"].median())
    print("Persentase viral:", df["viral"].mean() * 100, "%")

    genre_summary.to_csv(BASE_DIR / "ringkasan_genre.csv")
    year_summary.to_csv(BASE_DIR / "ringkasan_tahun_rilis.csv")

    # 3. Deteksi outlier global dengan aturan 1,5 x IQR
    q1 = df["streams"].quantile(0.25)
    q3 = df["streams"].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df["streams"] < lower) | (df["streams"] > upper)].copy()

    print("\\n=== DETEKSI OUTLIER GLOBAL ===")
    print(f"Q1={q1:,.2f}; Q3={q3:,.2f}; IQR={iqr:,.2f}")
    print(f"Batas bawah={lower:,.2f}; batas atas={upper:,.2f}")
    print("Jumlah potensi outlier:", len(outliers))
    print("\\n10 streams tertinggi:\\n",
          df.nlargest(10, "streams")[["track_id", "genre", "release_year", "streams", "viral"]])

    # 4. Outlier per genre, mengikuti whisker boxplot masing-masing kelompok
    outlier_rows = []
    for genre, part in df.groupby("genre"):
        gq1 = part["streams"].quantile(0.25)
        gq3 = part["streams"].quantile(0.75)
        giqr = gq3 - gq1
        g_low = gq1 - 1.5 * giqr
        g_high = gq3 + 1.5 * giqr
        group_outliers = part[
            (part["streams"] < g_low) | (part["streams"] > g_high)
        ]
        outlier_rows.append({
            "genre": genre,
            "jumlah_lagu": len(part),
            "Q1": gq1,
            "Q3": gq3,
            "IQR": giqr,
            "batas_bawah": g_low,
            "batas_atas": g_high,
            "jumlah_outlier_boxplot": len(group_outliers),
        })
    outlier_by_genre = pd.DataFrame(outlier_rows).sort_values(
        "jumlah_outlier_boxplot", ascending=False
    )
    outlier_by_genre.to_csv(BASE_DIR / "ringkasan_outlier_per_genre.csv", index=False)

    # 5. Persiapan data grafik
    viral_rate = genre_summary["tingkat_viral"] * 100
    genre_order = viral_rate.index.tolist()
    log_streams = np.log10(df["streams"].clip(lower=1))
    box_data = [
        df.loc[df["genre"] == genre, "streams"].values
        for genre in genre_order
    ]

    # Bar chart: tingkat viral per genre
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.barh(viral_rate.index[::-1], viral_rate.values[::-1])
    ax.set_title("Tingkat Lagu Viral Berdasarkan Genre")
    ax.set_xlabel("Lagu viral (%)")
    ax.set_ylabel("Genre")
    ax.set_xlim(0, max(viral_rate) * 1.15)
    for position, value in enumerate(viral_rate.values[::-1]):
        ax.text(value + 0.8, position, f"{value:.1f}%", va="center", fontsize=8)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "01_bar_tingkat_viral_genre.png", dpi=180)
    plt.close(fig)

    # Line chart: rata-rata streams berdasarkan kelompok tahun rilis
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.plot(
        year_summary.index,
        year_summary["rata_rata_streams"] / 1_000_000,
        marker="o",
    )
    ax.set_title("Rata-rata Streams per Lagu Berdasarkan Tahun Rilis")
    ax.set_xlabel("Tahun rilis")
    ax.set_ylabel("Rata-rata streams (juta)")
    ax.set_xticks(year_summary.index)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "02_line_rata_streams_tahun_rilis.png", dpi=180)
    plt.close(fig)

    # Scatter plot: danceability dan streams. Sumbu Y log agar rentang terbaca.
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    points = ax.scatter(
        df["danceability"], df["streams"],
        c=df["viral"], alpha=0.45, s=15
    )
    ax.set_yscale("log")
    ax.set_title("Hubungan Danceability dan Streams")
    ax.set_xlabel("Danceability (0–1)")
    ax.set_ylabel("Streams (skala log)")
    colorbar = fig.colorbar(points, ax=ax)
    colorbar.set_label("Label viral (0 = tidak, 1 = viral)")
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "03_scatter_danceability_streams.png", dpi=180)
    plt.close(fig)

    # Histogram: log10 streams untuk membaca distribusi yang sangat menceng.
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    ax.hist(log_streams, bins=40)
    ax.set_title("Distribusi Jumlah Streams (Log10)")
    ax.set_xlabel("Log10 jumlah streams")
    ax.set_ylabel("Jumlah lagu")
    ax.grid(True, axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "04_histogram_log_streams.png", dpi=180)
    plt.close(fig)

    # Boxplot: distribusi streams per genre pada skala log.
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(box_data, vert=False, tick_labels=genre_order, showfliers=True)
    ax.set_xscale("log")
    ax.set_title("Sebaran Streams per Genre (Boxplot, Skala Log)")
    ax.set_xlabel("Streams (skala log)")
    ax.set_ylabel("Genre")
    ax.grid(True, axis="x", alpha=0.2)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "05_boxplot_streams_genre.png", dpi=180)
    plt.close(fig)

    # Dashboard 2 x 2: empat grafik dalam satu figure.
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    ax = axes[0, 0]
    ax.barh(viral_rate.index[::-1], viral_rate.values[::-1])
    ax.set_title("Tingkat Viral per Genre")
    ax.set_xlabel("Lagu viral (%)")
    ax.set_ylabel("Genre")

    ax = axes[0, 1]
    ax.plot(
        year_summary.index,
        year_summary["rata_rata_streams"] / 1_000_000,
        marker="o",
    )
    ax.set_title("Rata-rata Streams menurut Tahun Rilis")
    ax.set_xlabel("Tahun rilis")
    ax.set_ylabel("Streams (juta)")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.2)

    ax = axes[1, 0]
    ax.hist(log_streams, bins=35)
    ax.set_title("Distribusi Streams (Log10)")
    ax.set_xlabel("Log10 streams")
    ax.set_ylabel("Jumlah lagu")

    ax = axes[1, 1]
    ax.boxplot(box_data, vert=False, tick_labels=genre_order, showfliers=True)
    ax.set_xscale("log")
    ax.set_title("Sebaran Streams per Genre")
    ax.set_xlabel("Streams (skala log)")
    ax.set_ylabel("Genre")
    ax.grid(True, axis="x", alpha=0.2)

    fig.suptitle("Dashboard Ringkas — Analisis Lagu Viral", fontsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(CHART_DIR / "06_dashboard_ringkas.png", dpi=180)
    plt.close(fig)

    print("\\nSelesai. Grafik tersimpan di:", CHART_DIR)
    print("Ringkasan CSV tersimpan di:", BASE_DIR)

if __name__ == "__main__":
    main()
