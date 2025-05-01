from sqlalchemy import Column, String, Integer
from .database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    rut = Column(String(12), primary_key=True, index=True)  # Ej: 12.345.678-9
    nombre_completo = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    curso = Column(String(50), nullable=False)