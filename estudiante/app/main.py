from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudiantes/", response_model=schemas.EstudianteOut)
def crear_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    nuevo_estudiante = models.Estudiante(**estudiante.dict())
    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)
    return nuevo_estudiante

@app.get("/estudiantes/", response_model=list[schemas.EstudianteOut])
def listar_estudiantes(db: Session = Depends(get_db)):
    return db.query(models.Estudiante).all()

@app.get("/estudiantes/{rut}", response_model=schemas.EstudianteOut)
def obtener_estudiante(rut: str, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter_by(rut=rut).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante
