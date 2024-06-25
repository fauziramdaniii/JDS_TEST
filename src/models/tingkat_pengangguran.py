# src/model/tingkat_pengangguran.py

from sqlalchemy import Column, Integer, String, Float
from src.config.database import Base

class TingkatPengangguran(Base):
    __tablename__ = "tingkat_pengangguran"

    id = Column(Integer, primary_key=True, index=True)
    kode_provinsi = Column(Integer)
    nama_provinsi = Column(String)
    pendidikan = Column(String)
    tingkat_pengangguran_terbuka = Column(Float)
    satuan = Column(String)
    tahun = Column(Integer)
