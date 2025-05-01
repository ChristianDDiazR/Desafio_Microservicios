from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import models, schemas
from databases import SessionLocal, engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudiantes/", response_model=schemas.EstudianteResponse)
def crear_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    db_est = models.Estudiante(**estudiante.dict())
    db.add(db_est)
    db.commit()
    db.refresh(db_est)
    return db_est

@app.get("/estudiantes/", response_model=list[schemas.EstudianteResponse])
def obtener_estudiantes(db: Session = Depends(get_db)):
    return db.query(models.Estudiante).all()

@app.get("/estudiantes/{rut}", response_model=schemas.EstudianteResponse)
def obtener_estudiante(rut: str, db: Session = Depends(get_db)):
    est = db.query(models.Estudiante).filter(models.Estudiante.rut == rut).first()
    if not est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return est
