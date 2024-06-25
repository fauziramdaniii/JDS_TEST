# src/routes/tingkat_pengangguran.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import SessionLocal
from src.models.tingkat_pengangguran import TingkatPengangguran

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tingkat_pengangguran/")
def read_tingkat_pengangguran(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pengangguran = db.query(TingkatPengangguran).offset(skip).limit(limit).all()
    return pengangguran
