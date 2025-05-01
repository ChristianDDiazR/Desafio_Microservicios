from sqlalchemy.orm import Session
from . import models, schemas

def crear_estudiante(db: Session, estudiante: schemas.EstudianteCreate):
    db_estudiante = models.Estudiante(
        rut=estudiante.rut,
        nombre_completo=estudiante.nombre_completo,
        edad=estudiante.edad,
        curso=estudiante.curso
    )
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

def obtener_estudiantes(db: Session):
    return db.query(models.Estudiante).all()

def obtener_estudiante_por_rut(db: Session, rut: str):
    return db.query(models.Estudiante).filter(models.Estudiante.rut == rut).first()
