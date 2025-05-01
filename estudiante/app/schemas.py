from pydantic import BaseModel

class EstudianteBase(BaseModel):
    rut: str
    nombre: str
    edad: int
    curso: str

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    class Config:
        orm_mode = True