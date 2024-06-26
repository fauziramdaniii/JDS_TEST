#src/routes/pengangguran.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.config.database import get_db
from src.models.pengangguran import TingkatPengangguran
from src.schemas.pengangguran import Pengangguran

router = APIRouter()

@router.get("/pengangguran/tahun/{tahun}", response_model=List[Pengangguran])
def get_pengangguran_by_year(tahun: int, db: Session = Depends(get_db)):
    result = db.query(TingkatPengangguran).filter(TingkatPengangguran.tahun == tahun).all()
    if not result:
        raise HTTPException(status_code=404, detail="Data not found")
    return result

@router.get("/pengangguran/pendidikan/{pendidikan}", response_model=List[Pengangguran])
def get_pengangguran_by_education(pendidikan: str, db: Session = Depends(get_db)):
    result = db.query(TingkatPengangguran).filter(TingkatPengangguran.pendidikan.ilike(pendidikan)).all()
    if not result:
        raise HTTPException(status_code=404, detail="Data not found")
    return result

@router.get("/pengangguran/tahun/{tahun}/pendidikan/{pendidikan}", response_model=List[Pengangguran])
def get_pengangguran_by_year_and_education(tahun: int, pendidikan: str, db: Session = Depends(get_db)):
    result = db.query(TingkatPengangguran).filter(
        TingkatPengangguran.tahun == tahun,
        TingkatPengangguran.pendidikan.ilike(pendidikan)
    ).all()
    if not result:
        raise HTTPException(status_code=404, detail="Data not found")
    return result
