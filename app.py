import streamlit as st
import pandas as pd

# ==========================
# KONFIGURASI HALAMAN
# ==========================

st.set_page_config(
    page_title="Dashboard Elektrifikasi Desa",
    layout="wide"
)

# ==========================
# MEMBACA EXCEL SEKALI SAJA
# ==========================

df = pd.read_excel(
    "Book1.xlsx",
    header=1
)

# ==========================
# HEADER
# ==========================

st.image(
    "listrik.jpg",
    use_container_width=True
)

st.title(
    "Dashboard Elektrifikasi Desa"
)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("LISDES KALTENG")

menu = st.sidebar.radio(
    "Menu Utama",
    [
        "Ringkasan",
        "Lokasi & Desa",
        "Rencana Tahunan",
        "Daftar Pekerjaan"
    ]
)

# ==========================
# MENU RINGKASAN
# ==========================

if menu == "Ringkasan":

    st.header("Dashboard Ringkasan")

    jumlah_provinsi = df["PROVINSI"].value_counts()

    jumlah_provinsi = jumlah_provinsi[
        jumlah_provinsi > 1
    ]

    st.subheader(
        "Jumlah Desa yang Sudah Berlistrik di Tiap Provinsi"
    )

    st.bar_chart(jumlah_provinsi)

    st.subheader("Contoh Data")

    st.dataframe(df.head())

# ==========================
# MENU LOKASI
# ==========================

elif menu == "Lokasi & Desa":

    st.title("Pencarian Lokasi Desa")

    desa = st.selectbox(
        "Pilih Desa",
        sorted(df["DESA"].dropna().unique())
    )

    hasil = df[df["DESA"] == desa]

    st.write(
        "### Informasi Lokasi"
    )

    st.write(
        "Provinsi:",
        hasil.iloc[0]["PROVINSI"]
    )

    st.write(
        "Kabupaten:",
        hasil.iloc[0]["KABUPATEN"]
    )

    st.write(
        "Kecamatan:",
        hasil.iloc[0]["KECAMATAN"]
    )

    st.write(
        "Desa:",
        hasil.iloc[0]["DESA"]
    )

# ==========================
# MENU TAHUNAN
# ==========================

elif menu == "Rencana Tahunan":

    st.header("Grafik Tahunan")

    df_tahun = df.copy()

    df_tahun["Usulan Tahun Roadmap"] = pd.to_numeric(
        df_tahun["Usulan Tahun Roadmap"],
        errors="coerce"
    )

    df_tahun = df_tahun.dropna(
        subset=["Usulan Tahun Roadmap"]
    )

    df_tahun["Usulan Tahun Roadmap"] = (
        df_tahun["Usulan Tahun Roadmap"]
        .astype(int)
        .astype(str)
    )

    jumlah_tahun = (
        df_tahun["Usulan Tahun Roadmap"]
        .value_counts()
        .sort_index()
    )

    st.subheader(
        "Jumlah Desa Berdasarkan Tahun Roadmap"
    )

    st.line_chart(jumlah_tahun)

# ==========================
# MENU PEKERJAAN
# ==========================

elif menu == "Daftar Pekerjaan":

    st.header("Daftar Pekerjaan")

    st.dataframe(df)