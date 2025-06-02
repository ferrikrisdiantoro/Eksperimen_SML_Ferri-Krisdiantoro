# Eksperimen_SML_Nama-siswa

Repositori ini dibuat untuk memenuhi **Kriteria 1** dari submission kelas **Machine Learning for Software Engineering (MSML)**, yang berfokus pada eksperimen awal terhadap dataset pelatihan.

## Tujuan

Melakukan eksplorasi dan eksperimen awal terhadap dataset pelatihan secara manual sebagai dasar untuk proses otomatisasi selanjutnya. Eksperimen dilakukan menggunakan **Template Eksperimen MSML**, dan hasil eksplorasi akan digunakan sebagai dasar pembuatan file preprocessing otomatis.

## Struktur Direktori

```
Eksperimen_SML_Ferri-Krisdiantoro/
├── .workflow/                        
├── obesity-classification_raw.csv 
├── requirements.txt        
├── preprocessing/
│   ├── Eksperimen_Ferri-Krisdiantoro.ipynb  
│   ├── automate_Ferri-Krisdiantoro.py      
│   └── obesity-classification_preprocessing.csv  
```

## Rincian File

- **Eksperimen_Ferri-Krisdiantoro.ipynb**  
  Notebook berisi eksplorasi manual terhadap dataset, mencakup:
  - Data Loading
  - Exploratory Data Analysis (EDA)
  - Data Preprocessing

- **automate_Ferri-Krisdiantoro.py**  
  Script Python untuk otomatisasi preprocessing data. Script ini mengonversi proses manual dari notebook menjadi fungsi yang dapat dijalankan untuk menghasilkan dataset siap latih. 

- **obesity-classification_raw.csv**  
  File berisi dataset mentah sebagai input awal.

- **obesity-classification_preprocessing.csv**  
  File hasil dari proses preprocessing otomatis/manual.

- **.workflow/**  
  Folder opsional yang berisi konfigurasi GitHub Actions. Jika digunakan, proses preprocessing dapat dilakukan otomatis saat terjadi perubahan atau trigger tertentu di repositori.

## Penilaian Kriteria

| Level     | Deskripsi                                                                 |
|-----------|---------------------------------------------------------------------------|
| Reject    | Tidak memenuhi tahapan eksplorasi dan preprocessing.                     |
| Basic     | Eksplorasi manual: data loading, EDA, dan preprocessing di notebook.     |
| Skilled   | Menambahkan script `automate_*.py` untuk preprocessing otomatis.         |
| Advance   | Menambahkan GitHub Actions (`.workflow`) untuk otomatisasi preprocessing.|

## Menjalankan Automatisasi (Skilled)

Untuk menjalankan preprocessing otomatis:

```bash
python preprocessing/automate_Ferri-Krisdiantoro.py
```

Script ini akan:
1. Membaca dataset mentah dari `obesity-classification_raw.csv`
2. Melakukan preprocessing sesuai eksperimen
3. Menyimpan output ke `obesity-classification_preprocessing.csv`

