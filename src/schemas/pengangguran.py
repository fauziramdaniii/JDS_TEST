from pydantic import BaseModel

class Pengangguran(BaseModel):
    id: int
    nama_provinsi: str
    pendidikan: str
    satuan: str
    kode_provinsi: int
    tingkat_pengangguran_terbuka: int
    tahun: int

    class Config:
        orm_mode = True
