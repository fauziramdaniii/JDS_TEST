#main.py
from fastapi import FastAPI
from src.config.database import Base, engine
from src.routes.pengangguran import router as pengangguran_router

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Hello": "Welcome to our chart of unemployment",
        "Endpoints": {
            "API Root": "/api/",
            "Pengangguran by Year": "/api/pengangguran/tahun/{tahun}",
            "Pengangguran by Education": "/api/pengangguran/pendidikan/{pendidikan}",
            "Pengangguran by Year and Education": "/api/pengangguran/tahun/{tahun}/pendidikan/{pendidikan}"
        },
        "For Documentation Test Is" : "http://127.0.0.1:8000/docs"
    }

# Include routers
app.include_router(pengangguran_router, prefix="/api", tags=["Pengangguran"])

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
