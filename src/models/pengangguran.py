#src/models/unemployment.py
from sqlalchemy import Column, Integer, String
from src.config.database import Base

class TingkatPengangguran(Base):
    __tablename__ = "tingkat_pengangguran"

    id = Column(Integer, primary_key=True, index=True)
    nama_provinsi = Column(String, index=True)
    pendidikan = Column(String, index=True)
    satuan = Column(String)
    kode_provinsi = Column(Integer)
    tingkat_pengangguran_terbuka = Column(Integer)
    tahun = Column(Integer)
