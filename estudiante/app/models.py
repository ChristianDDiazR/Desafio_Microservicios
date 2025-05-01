from sqlalchemy import Column, String, Integer
from databases import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    rut = Column(String(20), primary_key=True, index=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    curso = Column(String(50))