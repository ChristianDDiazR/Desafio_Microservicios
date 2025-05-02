from pydantic import BaseModel

class EvaluacionBase(BaseModel):
    id: str
    rut_estudiante: str
    semestre: str
    asignatura: str
    evaluacion: float

class EvaluacionCreate(EvaluacionBase):
    pass

class EvaluacionOut(EvaluacionBase):
    class Config:
        orm_mode = True
