from pydantic import BaseModel, constr

class EstudianteBase(BaseModel):
    nombre_completo: str
    edad: int
    curso: str

class EstudianteCreate(EstudianteBase):
    rut: constr(strip_whitespace=True, max_length=12)

class Estudiante(EstudianteBase):
    rut: str

    class Config:
        orm_mode = True
