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

@app.post("/evaluaciones/", response_model=schemas.EvaluacionOut)
def crear_evaluacion(evaluacion: schemas.EvaluacionCreate, db: Session = Depends(get_db)):
    nueva_evaluacion = models.Evaluacion(**evaluacion.dict())
    db.add(nueva_evaluacion)
    db.commit()
    db.refresh(nueva_evaluacion)
    return nueva_evaluacion

@app.get("/evaluaciones/", response_model=list[schemas.EvaluacionOut])
def listar_evaluaciones(db: Session = Depends(get_db)):
    return db.query(models.Evaluacion).all()

@app.get("/evaluaciones/{id}", response_model=schemas.EvaluacionOut)
def obtener_evaluacion(id: str, db: Session = Depends(get_db)):
    evaluacion = db.query(models.Evaluacion).filter_by(id=id).first()
    if not evaluacion:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")
    return evaluacion
