from sqlalchemy import Column, String, Float
from database import Base
from sqlalchemy.ext.declarative import declarative_base

class Evaluacion(Base):
    __tablename__ = "evaluaciones"

    id = Column(String(50), primary_key=True, index=True)
    rut_estudiante = Column(String(12), index=True)
    semestre = Column(String(20))
    asignatura = Column(String(100))
    evaluacion = Column(Float)
