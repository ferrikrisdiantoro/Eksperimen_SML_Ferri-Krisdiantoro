import pandas as pd

def hapus_outlier_iqr(df, kolom):
    Q1 = df[kolom].quantile(0.25)
    Q3 = df[kolom].quantile(0.75)
    IQR = Q3 - Q1
    batas_bawah = Q1 - 1.5 * IQR
    batas_atas = Q3 + 1.5 * IQR
    return df[(df[kolom] >= batas_bawah) & (df[kolom] <= batas_atas)]

def preprocess_data(path_csv):
    # Load data
    df = pd.read_csv(path_csv)

    # Hilangkan missing value
    df = df.dropna()

    # Hilangkan duplikat
    df = df.drop_duplicates()

    # Perbaiki nilai yang tidak konsisten
    df['Label'] = df['Label'].str.strip().str.title()
    df['Gender'] = df['Gender'].str.strip().str.title()

    # Hapus outlier kolom numerik
    df = hapus_outlier_iqr(df, 'Age')

    # Reset index agar rapi
    df = df.reset_index(drop=True)

    return df