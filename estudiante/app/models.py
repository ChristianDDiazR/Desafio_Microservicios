from sqlalchemy import Column, String, Integer
from database import Base
from sqlalchemy.ext.declarative import declarative_base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    rut = Column(String(12), primary_key=True, index=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    curso = Column(String(50))
