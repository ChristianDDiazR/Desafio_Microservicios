from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

# Crear la tabla si no existe
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Microservicio Estudiante")

# Dependencia para obtener sesión de BD
get_db = database.get_db

@app.get("/")
def read_root():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return {"message": "Conexión a MySQL exitosa"}
    except mysql.connector.Error as err:
        return {"error": f"No se pudo conectar a MySQL: {err}"}

@app.post("/estudiantes/", response_model=schemas.Estudiante)
def crear_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    db_est = crud.obtener_estudiante_por_rut(db, rut=estudiante.rut)
    if db_est:
        raise HTTPException(status_code=400, detail="El estudiante con ese RUT ya existe")
    return crud.crear_estudiante(db, estudiante)

@app.get("/estudiantes/", response_model=list[schemas.Estudiante])
def listar_estudiantes(db: Session = Depends(get_db)):
    return crud.obtener_estudiantes(db)

@app.get("/estudiantes/{rut}", response_model=schemas.Estudiante)
def obtener_estudiante(rut: str, db: Session = Depends(get_db)):
    estudiante = crud.obtener_estudiante_por_rut(db, rut=rut)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante
