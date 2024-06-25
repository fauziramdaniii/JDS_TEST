# main.py

from fastapi import FastAPI
from src.routes import tingkat_pengangguran
from src.config.database import Base, engine

app = FastAPI()

# Include routers
app.include_router(tingkat_pengangguran.router)

# Create tables
Base.metadata.create_all(bind=engine)
