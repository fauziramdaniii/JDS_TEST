# Insert Into Table Pengangguran
import pandas as pd
import sys
import os

# # Tambahkan path root proyek ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# PostgreSQL database connection details
from src.config.database import get_engine
engine = get_engine()

# Path to your Excel file
excel_file = 'src/dataset/Dataset_TingkatPengangguran.xlsx'

try:
    # Read Excel file
    df = pd.read_excel(excel_file, sheet_name='data')  # Adjust sheet_name as needed

    # Clean column names (strip any leading/trailing whitespaces)
    df.columns = df.columns.str.strip()

    # Rename columns to match PostgreSQL table columns
    df.columns = ["id", "kode_provinsi", "nama_provinsi", "pendidikan", "tingkat_pengangguran_terbuka", "satuan", "tahun"]

    # Insert data into PostgreSQL table
    df.to_sql('tingkat_pengangguran', engine, if_exists='append', index=False, method='multi')

    print("Data berhasil dimasukkan ke PostgreSQL!")

except Exception as e:
    print(f"Error: {e}")
