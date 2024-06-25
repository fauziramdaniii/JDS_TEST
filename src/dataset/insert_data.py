# import sys
# import os
# import pandas as pd
# from sqlalchemy import create_engine

# # Tambahkan path root proyek ke sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from src.config.database import get_engine  # Import fungsi koneksi dari database.py

# # Koneksi ke database PostgreSQL
# engine = get_engine()

# # Baca file CSV dengan delimiter yang benar
# csv_file = "src/dataset/Dataset_JumlahSekolahDasar.csv"  # Sesuaikan path

# # Mencoba membaca file CSV dan mencetak kolomnya
# try:
#     df = pd.read_csv(csv_file, delimiter=';')  # Gunakan ; sebagai delimiter
#     print("Kolom yang terdeteksi oleh Pandas:", df.columns)

#     # Hapus spasi tambahan pada nama kolom
#     df.columns = df.columns.str.strip()

#     # Buat dataframe hanya dengan kolom yang diperlukan
#     df = df[["Kode Wilayah", "Wilayah", "Tahun", "Jumlah Sekolah"]]

#     # Ubah nama kolom agar sesuai dengan nama kolom di tabel PostgreSQL
#     df.columns = ["kode_wilayah", "wilayah", "tahun", "jumlah_sekolah"]

#     # Insert data ke tabel PostgreSQL
#     df.to_sql('sekolah_dasar', engine, if_exists='append', index=False)

#     print("Data berhasil dimasukkan ke PostgreSQL!")
# except KeyError as e:
#     print(f"KeyError: {e}")
#     print("Kolom yang tersedia di CSV adalah:", df.columns)
# except Exception as e:
#     print(f"Error: {e}")

# Insert Into Table jumlah_pencari_kerja
# import sys
# import os
# import pandas as pd
# from sqlalchemy import create_engine

# # Add project root path to sys.path if not already added
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# # Import database connection function from database.py
# from src.config.database import get_engine

# # PostgreSQL database connection
# engine = get_engine()

# # Path to your CSV file
# csv_file = "src/dataset/Dataset_JumlahPencariKerja.csv"

# try:
#     # Read CSV file with correct delimiter (semicolon in your case)
#     df = pd.read_csv(csv_file, delimiter=';')

#     # Print detected columns for verification
#     print("Kolom yang terdeteksi oleh Pandas:", df.columns)

#     # Clean column names by stripping whitespace
#     df.columns = df.columns.str.strip()

#     # Ensure the exact column name exists in the DataFrame
#     required_columns = ["Kode Wilayah", "Wilayah", "Tahun", "Jumlah Pencari Kerja"]
#     for col in required_columns:
#         if col not in df.columns:
#             raise KeyError(f"'{col}' not found in CSV columns.")

#     # Select only necessary columns
#     df = df[required_columns]

#     # Rename columns to match PostgreSQL table columns
#     df.columns = ["kode_wilayah", "wilayah", "tahun", "jumlah_pencari_kerja"]

#     # Insert data into PostgreSQL table
#     df.to_sql('jumlah_pencari_kerja', engine, if_exists='append', index=False)

#     print("Data berhasil dimasukkan ke PostgreSQL!")
# except KeyError as e:
#     print(f"KeyError: {e}")
#     print("Kolom yang tersedia di CSV adalah:", df.columns)
# except Exception as e:
#     print(f"Error: {e}")


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
